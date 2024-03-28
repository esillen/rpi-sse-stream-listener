from time import sleep
try:
    import RPi.GPIO as GPIO
    
except RuntimeError:
    print("Error importing RPi.GPIO! This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

BLINK_TIME_SECONDS = 1
PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:  
    while True: 
        print("on") 
        GPIO.output(PIN, 1)         # set GPIO24 to 1/GPIO.HIGH/True  
        sleep(0.5)  
        print("off") 
        GPIO.output(PIN, 0)         # set GPIO24 to 0/GPIO.LOW/False  
        sleep(0.5)                 # wait half a second  
  
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()   
