import RPi.GPIO as GPIO
import time
import adafruit_adxl34x
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
#1 side//side
#0 forward/backward

while True:
        print("%f"%accelerometer.acceleration[0])

        if accelerometer.acceleration[0] > 1:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(18,GPIO.OUT)
            print ("led on")
            GPIO.output(18,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18,GPIO.LOW)


## TODO - wire a button to begin recording to csv file.
