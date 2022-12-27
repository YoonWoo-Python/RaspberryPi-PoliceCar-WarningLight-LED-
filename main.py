import RPi.GPIO as gpio
import time

ledBlue = 2
ledRed = 21
swPin = 16

gpio.setmode(gpio.BCM)
gpio.setup(ledBlue, gpio.OUT)
gpio.setup(ledRed, gpio.OUT)
gpio.setup(swPin, gpio.IN, pull_up_down=gpio.PUD_DOWN)

swValue = 0
swState = 0

try:
    while 1:
        swValue = gpio.input(swPin)
        if swValue == 1:
            if swState == 0:
                swState = 1
            else:
                swState = 0
            time.sleep(0.5)
            print(swState)
            time.sleep(0.1)

        if swState == 1:        
            gpio.output(ledRed, gpio.LOW)
            gpio.output(ledBlue, gpio.HIGH)
            time.sleep(0.3)
            gpio.output(ledRed, gpio.HIGH)
            gpio.output(ledBlue, gpio.LOW)
            time.sleep(0.3)
        else:
            gpio.output(ledRed, gpio.LOW)
            gpio.output(ledBlue, gpio.LOW)           

except KeyboardInterrupt:
    pass

gpio.cleanup()