import RPi.GPIO as GPIO
import time


def upper_broken():
    upper_green_led = 14
    upper_red_led = 15
    under_green_led = 16
    under_red_led = 17
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(upper_green_led, GPIO.OUT)
    GPIO.setup(upper_red_led, GPIO.OUT)
    GPIO.setup(under_green_led, GPIO.OUT)
    GPIO.setup(under_red_led, GPIO.OUT)

    GPIO.output(upper_red_led, True)
    GPIO.output(upper_green_led, False)
    GPIO.output(under_red_led, False)
    GPIO.output(under_green_led, True)

def under_broken():
    upper_green_led = 14
    upper_red_led = 15
    under_green_led = 16
    under_red_led = 17
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(upper_green_led, GPIO.OUT)
    GPIO.setup(upper_red_led, GPIO.OUT)
    GPIO.setup(under_green_led, GPIO.OUT)
    GPIO.setup(under_red_led, GPIO.OUT)

    GPIO.output(upper_red_led, False)
    GPIO.output(upper_green_led, True)
    GPIO.output(under_red_led, True)
    GPIO.output(under_green_led, False)

def both_broken():
    upper_green_led = 14
    upper_red_led = 15
    under_green_led = 16
    under_red_led = 17
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(upper_green_led, GPIO.OUT)
    GPIO.setup(upper_red_led, GPIO.OUT)
    GPIO.setup(under_green_led, GPIO.OUT)
    GPIO.setup(under_red_led, GPIO.OUT)

    GPIO.output(upper_red_led, True)
    GPIO.output(upper_green_led, False)
    GPIO.output(under_red_led, True)
    GPIO.output(under_green_led, False)

def normal():
    upper_green_led = 14
    upper_red_led = 15
    under_green_led = 16
    under_red_led = 17
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(upper_green_led, GPIO.OUT)
    GPIO.setup(upper_red_led, GPIO.OUT)
    GPIO.setup(under_green_led, GPIO.OUT)
    GPIO.setup(under_red_led, GPIO.OUT)

    GPIO.output(upper_red_led, False)
    GPIO.output(upper_green_led, True)
    GPIO.output(under_red_led, False)
    GPIO.output(under_green_led, True)
def close():
    upper_green_led = 14
    upper_red_led = 15
    under_green_led = 16
    under_red_led = 17
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(upper_green_led, GPIO.OUT)
    GPIO.setup(upper_red_led, GPIO.OUT)
    GPIO.setup(under_green_led, GPIO.OUT)
    GPIO.setup(under_red_led, GPIO.OUT)

    GPIO.output(upper_red_led, True)
    GPIO.output(upper_green_led, False)
    GPIO.output(under_red_led, True)
    GPIO.output(under_green_led, False)
