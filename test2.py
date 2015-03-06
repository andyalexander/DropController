import wiringpi2 as wiringpi
from time import sleep



pin1 = 0
pin2 = 1


wiringpi.wiringPiSetup()

wiringpi.pinMode(pin1,1)
#wiringpi.pinMode(pin2,1)

wiringpi.digitalWrite(pin1,1)
sleep(5)
wiringpi.digitalWrite(pin1,0) 
