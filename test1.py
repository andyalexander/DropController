import wiringpi
from time import sleep

gpio = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO)  
shutterpin = 12
solenoidpin = 13
wait = 5

print('should be using pins 11 and 12 on the header (corresponding to GPIO17 and GPIO18')

gpio.pinMode(shutterpin,gpio.OUTPUT)  
gpio.pinMode(solenoidpin,gpio.OUTPUT)
wiringpi.pinMode(shutterpin,1)
wiringpi.pinMode(solenoidpin,1)

print('setting pin 17 high')
gpio.digitalWrite(solenoidpin,gpio.HIGH)                # open the solenoid first time
sleep(wait)                  
print('setting pin 17 low')                             # delay for drop to form
gpio.digitalWrite(solenoidpin,gpio.LOW)                 # close solenoid

sleep(wait)                                               # wait for the drop to fall some way

print('setting pin 18 high')
gpio.digitalWrite(solenoidpin,gpio.HIGH)                # second drop open solenoid
sleep(wait)                  
print('setting pin 18 low')                             # second drop delay
gpio.digitalWrite(solenoidpin,gpio.LOW)                 # close solenoid
