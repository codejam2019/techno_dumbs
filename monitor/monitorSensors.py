'author=keerthi'
'Monitor data to alert system to know about sensor issue'
import os
import datetime
dataFolder = "/tmp/data"
seconsGap = 10*60
ep = datetime.datetime(1970,1,1,0,0,0)
currentEpochTime =  (datetime.datetime.utcnow()- ep).total_seconds()
print currentEpochTime
errorData = ""
#1575105548.07
def readFoldersandFiles():
    errorData = ""
    for root,d_names,f_names in os.walk(dataFolder):
        if len(f_names) > 0:
            for fName in f_names:
                createdDateOfFile = os.path.getmtime(root + "/" + fName)
                #print createdDateOfFile
                #print datetime.datetime.fromtimestamp(createdDateOfFile)
                if currentEpochTime - createdDateOfFile > seconsGap:
                    print root 
                    #print createdDateOfFile
                    folderList = root.split("/")
                    cityName = folderList[len(folderList) -3].split("=")[1]
                    sensorId = folderList[len(folderList) -2].split("=")[1]
                    #print cityName
                    errorData = errorData +  cityName + " and " + sensorId + " gone offline.\n"
                    #print sensorId

    errorfile = open("error.log","w")
    errorfile.write(errorData)

if __name__ == "__main__":
    readFoldersandFiles()
        