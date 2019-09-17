import RPi.GPIO as GPIO
import time
import board
import busio
import adafruit_adxl34x
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
#1 side//side

while True:
        print("%f"%accelerometer.acceleration[0])
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)
        if accelerometer.acceleration[0] > 1:
            print ("led on")
            GPIO.output(18,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18,GPIO.LOW)


