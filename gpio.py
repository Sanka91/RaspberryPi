import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.getmode()


GPIO.setup(16, GPIO.IN, GPIO.PUD_UP)

input_value = GPIO.input(16)

print(input_value)

GPIO.cleanup()
