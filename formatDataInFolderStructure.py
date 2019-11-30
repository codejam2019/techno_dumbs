import csv
import json
import os
csvfile = open('/home/ubuntu/Documents/keerthicode/beach-weather-stations-automated-sensors_test.csv', 'r')
cityNames = {"0-5000" : "Delhi" ,"5001-8699" :
 "Hyderabad" ,"10000-16000" : "Pune","32000-39000" : "Mumbai"
  ,"40000-50000" : "Bangalore" }
path = "/tmp/data/"
if not os.path.exists(path):
    os.mkdir(path)
fieldnames = ("Sensor_Location","Timestamp","Temperature","Humidity","Rain_Intensity","Total_Rain","Wind Direction","Wind_Speed","Barometric_Pressure","Solar_Radiation","Measurement_ID")
reader = csv.DictReader( csvfile, fieldnames)
incrCount =0
incrId = 0
for row in reader:
    #jsonfile = open('data/file' + str(i) + '.json', 'w')
    print row

    for key1 in row.keys():
        print key1
        print row[key1]
    folderpath = path + "City-Chennai"
    for key in cityNames.keys():
        print(key)
        min = int(key.split("-")[0])
        max = int(key.split("-")[1])
        if min <= incrCount <= max:
           folderpath = path + "City=" + cityNames[key] 
    if not os.path.exists(folderpath)  :    
        os.mkdir(folderpath)
    sensorFolder ="SendorId=" + row["Sensor_Location"].replace(" ","") +  str(incrId)   
    if not os.path.exists(folderpath + "/" + sensorFolder)  :    
        os.mkdir(folderpath + "/" + sensorFolder) 
    dateFolder = "Date=" + row["Timestamp"].split(" ")[0].replace("/","-")    
    if not os.path.exists(folderpath + "/" + sensorFolder + "/" + dateFolder)  :    
        os.mkdir(folderpath  + "/" + sensorFolder + "/" + dateFolder)        
    print row["Measurement_ID"]    
    jsonfile = open(folderpath + "/" + sensorFolder + "/" + dateFolder +   "/" + row["Measurement_ID"]  + ".json","w")
    print jsonfile
    json.dump(row, jsonfile)
    incrCount = incrCount + 1
    incrId = incrId + 1
    if incrId >= 10 :
        incrId = 0