from gpsClass import SmartAVLGPS

myGPS = SmartAVLGPS()
myGPS.start()

while(True):
	print("---------GPS DATA-----------")
	dataList = myGPS.get_data()
	if dataList is not None:
		current_timestamp = dataList[0]
		current_latitude = dataList[1]
		current_longitude = dataList[2]
		current_speed = dataList[3]
		print("Timestamp: {}/{}/{} {:02}:{:02}:{:02}".format(
			current_timestamp.tm_day,
			current_timestamp.tm_mon,
			current_timestamp.tm_year,
			current_timestamp.tm_hour,
			current_timestamp.tm_min,
			current_timestamp.tm_sec))
		print("Latitude: 
	else
		print("No data to report")
	
	time_before_sleep = time.monotonic()
	while(time.monotonic() - time_before_sleep < 1.0):
		time.sleep(0.2) #Let the thread block instead of busy wait
