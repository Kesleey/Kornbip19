import os
import csv
from datetime import datetime
from os import path
import numpy as np


ROOT_DIR = os.path.dirname(os.path.abspath(os.curdir))
ROOT = ROOT_DIR.replace("\\", "/")

#create attendance csv
def createCSV(path):
    names = []
    list = os.listdir(ROOT + "/app/Uploads")
    for users in list:
        names.append(users)
    names = np.reshape(names,(-1,1))
    with open(path, 'w+',
            newline='') as file:
        header = ['Name of students']
        writer = csv.writer(file)
        writer.writerow(header)

        write = csv.writer(file)
        write.writerows(names)

def updateCSV(names,filePath): #filePath = C:\Users\Kesley\PycharmProjects\9315-kornbip19/Attendance.csv
    if path.exists(filePath):
        print("exists")
        tempFile = ROOT + '/app/temp.csv'
        today = datetime.today().strftime('%Y-%m-%d')

        with open(filePath , 'r') as read,\
        open(tempFile, 'w+' , newline='') as write:
            reader = csv.reader(read)
            writer = csv.writer(write)
            i = 0;

            for row in reader:
                if i == 0:
                    row.append(today)
                else:
                    if row[0] in names:
                        row.append('p')
                    else:
                        row.append('a')
                writer.writerow(row)
                i += 1;
        os.remove(filePath)
        os.rename(tempFile, filePath)
    else:
        print("nope!")
        createCSV(filePath)
        print("exists")
        tempFile = ROOT + '/app/temp.csv'
        today = datetime.today().strftime('%Y-%m-%d')

        with open(filePath, 'r') as read, \
                open(tempFile, 'w+', newline='') as write:
            reader = csv.reader(read)
            writer = csv.writer(write)
            i = 0;

            for row in reader:
                if i == 0:
                    row.append(today)
                else:
                    if row[0] in names:
                        row.append('p')
                    else:
                        row.append('a')
                writer.writerow(row)
                i += 1;
        os.remove(filePath)
        os.rename(tempFile, filePath)


#name = ['kesley','kesley']
#updateCSV(name, 'C:/Users/Kesley/PycharmProjects/9315-kornbip19/Attendance Report/Attendance.csv')