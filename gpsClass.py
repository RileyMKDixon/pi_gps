#Much of this class is adapted from Adafruit and the example code that
#they provide to their users for their hardware products.
#This script relies on their CircuitPython framework that the GPS uses
#to communicate through the GPIO pins of the Raspberry Pi.
#Communication is handled through the UART

import time
import board
import busio
import serial
import os
import threading

class SmartAVLGPS(threading.Thread):
		
	def __init__(self):
		threading.Thread.__init__(self)
		self.data_semaphore = threading.BoundedSemaphore(1)
		self.current_longitude = None
		self.current_latitude = None
		self.current_speed = None
		self.timestamp = None
		self.gps = None
		
	def run(self):
		self.connect_to_GPS_network()
		while(True):
			update_present = self.gps.update()
			if update_present:
				if self.gps.has_fix:
					self.update_data()
				else:
					print("No fix on GPS network")
			else:
				print("No update received.")
			
			#Enforce a 0.5s delay before next update. This is half of
			#The update period.
			time_before_sleep = time.monotonic()
			while(time.monotonic() - time_before_sleep < 0.5):
				time.sleep(0.1) #Let the thread block instead of busy wait
		
		
	def connect_to_GPS_network(self):
		UART = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)
		self.gps = adafruit_gps.GPS(UART, debug=False)
		#Initialize Communication
		self.gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
		self.gps.send_command(b'PMTK220,1000') #1000ms update period

	
	def knots_to_kmh(self, knots):
		return knots * 1.852
	
	#Compare the passed timestamp to the one currently stored in memory
	#If passed timestamp is newer, return 1
	#If passed timestamp is the same, return 0
	#If passed timestamp is older, return -1
	#Else return None as result is inconclusive
	def compare_timestamp(self, other_timestamp):
		result = None
		if(other_timestamp.tm_year == self.timestamp.tm_year):
			if(other_timestamp.tm_month == self.timestamp.tm_month):
				if(other_timestamp.tm_mday == self.timestamp.tm_mday):
					if(other_timestamp.tm_hour == self.timestamp.tm_hour):
						if(other_timestamp.tm_min == self.timestamp.tm_min):
							if(other_timestamp.tm_sec == self.timestamp.tm_sec):
								result = 0
							elif(other_timestamp.tm_sec > self.timestamp.tm_sec):
								result = 1
							else:
								result = -1
						elif(other_timestamp.tm_min > self.timestamp.tm_min):
							result = 1
						else:
							result = -1
					elif(other_timestamp.tm_hour > self.timestamp.tm_hour):
						result = 1
					else:
						result = -1
				elif(other_timestamp.tm_mday > self.timestamp.tm_mday):
					result = 1
				else:
					result = -1
			elif(other_timestamp.tm_mon > self.timestamp.tm_mon):
				result = 1
			else:
				result = -1
		elif(other_timestamp.tm_year > self.timestamp.tm_year):
			result = 1
		else:
			result = -1
		return result
		
		
	def update_data(self):
		self.data_semaphore.acquire()
		self.current_longitude = 0
		self.current_latitude = 0
		self.current_speed = None
		self.timestamp = None
		self.data_semaphare.release()
	
	
	def get_data(self):
		import copy
		self.data_semaphore.acquire()
		if (self.timestamp is not None and
		   self.current_longitude is not None and
		   self.current_longitude is not None and
		   self.current_speed is not None):
			data_list = [copy.deepcopy(self.timestamp), 
						copy.deepcopy(self.current_longitude),
						copy.deepcopy(self.current_latitude),
						copy.deepcopy(self.current_speed)]
		else:
			data_list = None
		self.data_semaphare.release()
		return data_list
		




