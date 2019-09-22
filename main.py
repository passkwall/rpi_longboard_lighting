import RPi.GPIO as GPIO
from gpiozero import Button
import time
import adafruit_adxl34x
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)
accelerometer = adafruit_adxl34x.ADXL345(i2c)
#1 side//side
#0 forward/backward

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.output(18,GPIO.LOW)

button_pressed = Button(23)


while True:

    x = accelerometer.acceleration[0]
    y = accelerometer.acceleration[1]
    z = accelerometer.acceleration[2]

    long_poll = []
    short_poll = []

    if len(short_poll) > 10:
        short_poll.pop(0)
        short_poll.append(x)
    else:
        short_poll.append(x)

    if len(long_poll) > 100:
        long_poll.pop(0)
        long_poll.append(x)
    else:
        long_poll.append(x)

    short_average = sum(an_array)/(len(an_array))
    long_average = sum(long_poll)/(len(long_poll))
    diff = short_average - long_average

    if diff > 1:
        GPIO.output(18,GPIO.HIGH)
        print("Braking!")
        GPIO.output(18,GPIO.LOW)
        time.sleep(1)