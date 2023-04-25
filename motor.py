import RPi.GPIO as GPIO
import time

in1 = 4
en = 3
in2 = 2

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p=GPIO.PWM(en, 100)

p.start(100)
GPIO.output(en, GPIO.HIGH)
GPIO.output(in1, GPIO.HIGH)
GPIO.output(in2, GPIO.LOW)
time.sleep(5)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.HIGH)
time.sleep(5)
