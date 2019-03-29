#Simple script to test gpsClass and to verify that is does infact
#run asyncronously from the main thread.
import time
from gpsClass import SmartAVLGPS

myGPS = SmartAVLGPS()
myGPS.start()

while(True):
	time_before_sleep = time.monotonic()
	#This wait period can be as long as we want, in fact we can just
	#arbitrarilly call myGPS.get_data()
	while(time.monotonic() - time_before_sleep < 1.0):
		time.sleep(0.5) #Let the thread block instead of busy wait
	print("---------GPS DATA-----------")
	dataList = myGPS.get_data()
	if dataList is not None:
		current_timestamp = dataList[0]
		current_latitude = dataList[1]
		current_longitude = dataList[2]
		current_speed = dataList[3]
		print("Timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
			current_timestamp.tm_mday,
			current_timestamp.tm_mon,
			current_timestamp.tm_year,
			current_timestamp.tm_hour,
			current_timestamp.tm_min,
			current_timestamp.tm_sec))
		print("Latitude: {0:.6f}".format(current_latitude))
		print("Longitude: {0:.6f}".format(current_longitude))
		print("Approx Speed: {0:.2f} km/h".format(current_speed*1.852))
	else:
		print("No data to report")
	
	
