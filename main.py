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
with open("log.csv", mode='r') as log_file:

    while True:
        button = button_pressed.wait_for_press()
        rec_mode.toggle_record(button)

        while rec_mode.record == True:
            GPIO.setwarnings(False)
            GPIO.setup(18,GPIO.OUT)
            GPIO.output(18,GPIO.HIGH)

            csv_writer = csv.writer(log_file)
            x = accelerometer.acceleration[0]
            y = accelerometer.acceleration[1]
            z = accelerometer.acceleration[2]
                            
            csv_writer.writerow([x,y,z, time.time()])
