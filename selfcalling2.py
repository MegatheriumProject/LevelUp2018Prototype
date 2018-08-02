import RPi.GPIO as GPIO
import time
import subprocess
import shlex
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
var=10

while 1:
    try:
        update=GPIO.input(17)
        print (update)
        command='sudo python ledpi.py'
        args=shlex.split(command)
        subprocess.call(args)
        time.sleep(5)
        if update == 1:
            command='git pull origin master'
            args=shlex.split(command)
            subprocess.call(args)
            print (var)
            print ("Actualizado")
            time.sleep(5)
            GPIO.output(18,GPIO.LOW)
            GPIO.output(25,GPIO.LOW)
    except:   
        print ("end")
        break
