#!/usr/bin/python
import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600)

Input = [0, 0, 0, 0, 0, 0]
print('Horizontal   Vertical  Shooting  Steering   Other   Pause')

def Update(Input): #UPDATES DATA READINGS
    ser.write(b'`')     #tells arduino it wants some readings
    val1 = ser.readline().strip() #reads all input at once as a string
    if (len(val1) != 0):          #makes sure not empty
        rawArray = val1.decode().split(' ')    #generates array with ' ' delimiter
        if (len(rawArray) == 6):           #gets rid of first garbage read
            Input[0] = int(rawArray[0])
            Input[1] = int(rawArray[1])
            Input[2] = int(rawArray[2])
            Input[3] = str(rawArray[3])
            Input[4] = int(rawArray[4])
            Input[5] = int(rawArray[5])
            return

def PrintList(Input):
    print(Input[0], '\t', Input[1])
    return

while 1:
    Update(Input)
    PrintList(Input)
    time.sleep(0.05)
    

    
  
   #val1 = ser.readline().strip() #reads all input at once as a string
    #if (len(val1) != 0):          #makes sure not empty
    #    testArray = str(val1).split(' ')    #generates array with ' ' delimiter
    #    if (len(testArray) == 6):           #gets 
    #        print (testArray)
    #       time.sleep(1)print('Reading...')
