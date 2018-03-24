import RPi.GPIO as GPIO
import pyrebase

PATH_LISTENING = '/GPIO_05'
GPIO_OUTPUT = 5
# config of Firebase
config = {
  "apiKey": "AIzaSyCpAaeOr0LqZCkeU5ZzN9xC7SeLzJRVY-M",
  "authDomain": "raspberryexperiment.firebaseapp.com",
  "databaseURL": "https://raspberryexperiment.firebaseio.com",
  "storageBucket": "raspberryexperiment.appspot.com"
}

# use the position on board as it's name
GPIO.setmode(GPIO.BOARD)

# tell raspberry : this is an output.
GPIO.setup(GPIO_OUTPUT,GPIO.OUT) 


firebase = pyrebase.initialize_app(config)
db = firebase.database()
''' use these to test:
gpio = db.child("GPIO").get()
print(gpio.val())
'''

def stream_handler(message):
    if message["data"]==True and message['path']==PATH_LISTENING:
        print ('ON!')
        GPIO.output(GPIO_OUTPUT, GPIO.HIGH)
    else:
        print ('Off...')
        GPIO.output(GPIO_OUTPUT, GPIO.LOW)

my_stream = db.child("GPIO").stream(stream_handler)

# my_stream.close() 