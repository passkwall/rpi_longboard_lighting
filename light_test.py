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
GPIO.output(18,GPIO.LOW)

class Record_mode:
    def __init__(self):
        self.record = False

    def toggle_record(self, button):
        if self.record == True and button == True:
            self.record = False
        elif self.record == False and button == True:
            self.record = True
    
    
rec_mode = Record_mode()

file_name = str(time.time()) + "_log.csv"
with open("out.csv", mode='r') as log_file:

    while True:
        time.sleep(.02)
        log = csv.reader(log_file)
        for row in log:
            x = row[0]
            short_avg = row[1]
            long_avg = row[2]
            diff = row[3]
            time = row[4]

            if diff > 1:
                GPIO.output(18,GPIO.HIGH)
                print("Braking!")
                GPIO.output(18,GPIO.LOW)
