#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
LEDS = [7, 11, 12, 13, 15, 16, 18, 22] #starts at red to green
Buzzer = 29
HealthLevel = 4

def SetLights(level):
    #fixes wrong levels
    if (level > 8):
        level = 8
    if (level < 0):
        level = 0
        
    #turn off all lights above level
    for i in range(7, level-1, -1):
        GPIO.output(LEDS[i], GPIO.LOW)
    #turn on all lights at and below level
    for i in range(level):
        GPIO.output(LEDS[i], GPIO.HIGH)

def TurnOff():
    for i in range(8):
        GPIO.output(LEDS[i], GPIO.LOW)
    GPIO.output(Buzzer, GPIO.LOW)

        
GPIO.setmode(GPIO.BOARD) # Number GPIOs by its physical location
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, GPIO.LOW)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, GPIO.LOW)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13, GPIO.LOW)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15, GPIO.LOW)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, GPIO.LOW)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.LOW)
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, GPIO.LOW)
GPIO.setup(29, GPIO.OUT)
GPIO.output(29, GPIO.LOW)

#testing
SetLights(HealthLevel)
GPIO.output(Buzzer, GPIO.HIGH)
time.sleep(2)
GPIO.output(Buzzer, GPIO.LOW)
HealthLevel = 1
SetLights(HealthLevel)

def loop():
    while 1:
        if (HealthLevel <= 1):
            #see if buzzer should be on or off (every half second)
            if (int((time.clock()*10))%2 == 0):
                GPIO.output(Buzzer, GPIO.HIGH)
            else:
                GPIO.output(Buzzer, GPIO.LOW)
            
#time.sleep(2)
#SetLights(3)
#time.sleep(2)
#SetLights(12)
#time.sleep(2)
#SetLights(-4)
#time.sleep(2)


def destroy(): # When program ending, the function is executed.
    TurnOff()

if __name__ == '__main__': # Program starting from here
    try:
        loop()
    except KeyboardInterrupt:
        TurnOff()



