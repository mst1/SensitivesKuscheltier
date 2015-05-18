from time import sleep

__author__ = 'Johannes'
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.output(37, GPIO.LOW)
GPIO.output(35, GPIO.LOW)
GPIO.output(33, GPIO.LOW)

GPIO.output(37, GPIO.HIGH)
sleep(1000)
GPIO.output(37, GPIO.LOW)
GPIO.output(35, GPIO.HIGH)
sleep(1000)
GPIO.output(35, GPIO.LOW)
GPIO.output(33, GPIO.HIGH)
sleep(1000)
GPIO.output(33, GPIO.LOW)
GPIO.output(35, GPIO.HIGH)
sleep(1000)
GPIO.output(35, GPIO.LOW)
GPIO.output(37, GPIO.HIGH)
sleep(1000)
GPIO.output(37, GPIO.LOW)

