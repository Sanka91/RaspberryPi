import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#GPIO.cleanup()

# read data using Pin GPIO21 
instance = dht11.DHT11(pin=16)

print("running")

while True:
    print("in while loop")
    result = instance.read()
    print(result.temperature)
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)

    time.sleep(1)
