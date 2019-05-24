import os
import csv
import ais
import shutil
import datetime

#path to source raw AIS data
path = 'AIS'
#path to destination of old Raw AIS data
dest = 'AIS\\old'
#path to destination of the final file
destFinal = 'AIS'
#Dict to search the convertion from MMSI to IMO
imos = {}


#lists to save the file raw information to append the IMO in the final file
listNew = []

#skips the first line of the csv file which contains text instead of the wanted values
flag = 0

#saves relation between IMO and MMSI to a dict
with open('IMO_MMSI_matched_v1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        if flag == 0 :
            flag = 1
        else :
            imos[row[1]]=row[0]
csvfile.close()

#Error number
#i = 0
#goes through the folder AISRawGomX4, decodes the ais, compares with the LUT, writes to a list if there is a match.
for root, dirs, files in os.walk(path):  
    for filename in files:
        new_path = path + '\\' + filename
        with open(new_path, 'r') as f:
            content = f.readlines()
            for line in content:
                
                aisCode = line.split('\\')

                #saves in a list only the AIS codes
                decode = aisCode[2].split(',')

                #if the code is correct
                try :
                    AIS = ais.decode(decode[5], 0)
              
                #if the code has an ERROR
                except :
                    #i+=1
                    #print ('Error')
                    #print (i)
                    break

                #if it exists in the LUT add to the original line the imo
                if str(AIS['mmsi']) in imos:
                    newLine = 'imo:' + imos[str(AIS['mmsi'])] + ',' + line
                    
                    #print(AIS['mmsi'])
                    #print(imos[str(AIS['mmsi'])])
                
                #if it does bit exist in the LUT add to the original line the imo = 0
                else :
                    newLine = 'imo:0,' + line

                listNew.append(newLine) 
                         
            f.close()

files = os.listdir(path)
for f in files:
    if f[-3:] == "ais":
        shutil.move(path+'/'+f, dest)

x = datetime.datetime.now().strftime('%Y%m%d')
fileName = destFinal +"\\" + x + ".ais"

#saves everything in the final file
with open(fileName, 'w+') as f:
    for code in listNew:
        f.write(code)
    f.close()

