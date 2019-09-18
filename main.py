import RPi.GPIO as GPIO
from gpiozero import Button
import time
import adafruit_adxl34x
import board
import busio
import csv
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
#1 side//side
#0 forward/backward

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)

button_pressed = Button(23)
print(button_pressed)

file_name = str(time.time()) + "_log.csv"
with open(file_name, mode='w') as log_file:
    csv_writer = csv.writer(log_file)
    while True:
        x = accelerometer.acceleration[0]
        y = accelerometer.acceleration[1]
        z = accelerometer.acceleration[2]
        button_pressed.wait_for_press()
        csv_writer.writerow([x,y,z])
        #print("%f"%accelerometer.acceleration[0])
        if x > 1:
            GPIO.setwarnings(False)
            GPIO.setup(18,GPIO.OUT)
            print ("led on")
            GPIO.output(18,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(18,GPIO.LOW)
