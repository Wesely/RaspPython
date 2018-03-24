import RPi.GPIO as GPIO
import time

# Which pin ? see :http://osoyoo.com/wp-content/uploads/2017/06/Raspberry-GPIO-Pins_B_plus.jpg
GPIO_OUTPUT = 5

# use the position on board as it's name
GPIO.setmode(GPIO.BOARD)

# tell raspberry : this is an output.
GPIO.setup(GPIO_OUTPUT,GPIO.OUT) 

while True :
    GPIO.output(GPIO_OUTPUT, GPIO.HIGH)
    time.sleep(0.2) # second
    GPIO.output(GPIO_OUTPUT, GPIO.LOW)
    time.sleep(0.2) # second
