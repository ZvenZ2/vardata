
def flash():
    try:
        from time import sleep
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        for i in range(20):
            GPIO.output(18, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(18, GPIO.LOW)
            sleep(0.1)
        GPIO.cleanup()
    except Exception as e:
        print("Could nor flash light")
        print(e)
