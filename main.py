from time import sleep
from sseclient import SSEClient
try:
    import RPi.GPIO as GPIO
    
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

NOTIFICATION_TIME_SECONDS = 10
PIN = 24
URL = 'http://mysite.com/sse_stream/'
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)

messages = SSEClient(URL)
for msg in messages:
    print("new message!")
    GPIO.output(PIN, GPIO.HIGH)
    sleep(NOTIFICATION_TIME_SECONDS)
    GPIO.output(PIN, GPIO.LOW)
