import RPi.GPIO as GPIO
import time
import subprocess
import shlex
var=10
while var > 0: 
    command='sudo python ledpi.py'
    args=shlex.split(command)
    subprocess.call(args)
    time.sleep(10)
    command='git pull origin master'
    args=shlex.split(command)
    subprocess.call(args)
    print (var)
    print ("Actualizado")

    var=var-1
    if var == 1:
        break
print ("end")
