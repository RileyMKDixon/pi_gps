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
	
	CONNECTION_TIMEOUT = 20
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.current_longitude = 0
		self.current_latitude = 0
		self.current_speed = None
		self.timestamp = None
		self.gps = None
		
	def run(self):
		connect_to_GPS_network()
		start_time = time.monotonic()
		while not gps.has_fix:
			if time.monotonic() - start_time > 20:
				raise IOError("GPS Failed To connect
		
		
	def connect_to_GPS_network(self):
		UART = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=3000)
		self.gps = adafruit_gps.GPS(uart, debug=False)
		#Initialize Communication
		self.gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')
		gps.send_command(b'PMTK220,1000') #1000ms update period
		currentTime
	
	#Waits until the GPS is connected back to the network.
	#Will wait indefinitely so it does not interfere with the rest
	#Of the operation of the device.
	def wait_for_GPS_connected(self):
		
	
	def knots_to_kmh(knots):
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
		
	def get_data(self):
		pass
		
		
	def update_data(self):
		pass
	
