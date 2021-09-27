import RPi.GPIO as GPIO
import time

upper_servo = 23
under_servo = 24

def upper_broken():
    upper_servo = 23
    under_servo = 24
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(upper_servo, GPIO.OUT)
    p = GPIO.PWM(upper_servo, 50)
    p.start(0)
    
    p.ChangeDutyCycle(2.5)
    print("0도")
    time.sleep(0.5)

    p.ChangeDutyCycle(12.5)
    print("180도")
    time.sleep(0.5)

    p.ChangeDutyCycle(2.5)
    print("0도")
    time.sleep(0.5)
    GPIO.cleanup()

def under_broken():
    upper_servo = 23
    under_servo = 24
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(under_servo, GPIO.OUT)
    p = GPIO.PWM(under_servo, 50)
    p.start(0)
    
    p.ChangeDutyCycle(2.5)
    print("0도")
    time.sleep(0.5)

    p.ChangeDutyCycle(12.5)
    print("180도")
    time.sleep(0.5)

    p.ChangeDutyCycle(2.5)
    print("0도")
    time.sleep(0.5)
    GPIO.cleanup()

def both_broken():
    upper_broken()
    under_broken()

