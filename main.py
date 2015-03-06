import wiringpi2 as wiringpi
from time import sleep
# from unittest.mock import Mock

# gpio = Mock()
# wiringpi = Mock()
    
# if __name__ == '__main__':

wiringpi.wiringPiSetup()									# use wiringpi layout 
shutterpin = 0 												# header pin 11
solenoidpin = 1 											# header pin 12
HIGH=1
LOW=0

wiringpi.pinMode(shutterpin,1)								# set both pins for output (0=in,1=out,2=pwm)
wiringpi.pinMode(solenoidpin,1)

# using s=ut + 0.5 at^2  where a=9.8, u=0, distance s is 0.4m; ->  0.4 = 0.5 * 9.8 t^2 => t = (0.4/9.8)^0.5

waterHeight = 0.4                                           # height in cm of solenoid above water
drop2Height = 0.02                                          # height of second drop when shutter fires

timeToWater = (waterHeight/(0.5*9.8))**0.5
shutterDelay = 0.07                                         # delay of shutter after first drop hits
shutterLag = 0.06                                           # shutter lag, 7D approx. 59ms

t1 = 0.06                                                   # solenoid open time for drop 1
t2 = 0.1                                                    # delay before second drop
t3 = 0.05                                                   # solenoid open time for drop 2
# t4 = 0.12                                                   # delay for shutter after second drop finished - from example
# t4 = timeToWater - t2 - t3 + shutterDelay                   # delay for shutter after second drop finished - constant delay after first drop
t4 = ((waterHeight - drop2Height)/(0.5*9.8))**0.5           # delay for shutter based on drop 2 height above the water
t4 = t4 - shutterLag                                        # adjust for the shutter lag, start things early :)

t5 = 0.1                                                    # shutter open time [this should just be long enough to fire the shutter, won't actually do anything else]

shutterTimeTotal = t2 + t3 + t4                             # total time before the shutter starts to fire (should just be timeToWater+shutterDelay)

print("Assumed time to water: {0:03.2f}s".format(timeToWater))
print("Elapsed time before shutter starts: {0:03.2f}s".format(shutterTimeTotal))
print("Elapsed time before shutter ends: {0:03.2f}s".format(shutterTimeTotal + shutterLag))
print("Second drop will be: {0:03.1f}cm above the water when shutter starts".format((waterHeight - 0.5*9.8*t4**2)*100))
print("Second drop will be: {0:03.1f}cm above the water when shutter ends".format((waterHeight - 0.5*9.8*(t4+shutterLag)**2)*100))
print("t4 delay: {0:03.2f}s (make sure this is >0)".format(t4))


wiringpi.digitalWrite(solenoidpin,HIGH)                # open the solenoid first time
sleep(t1)                                               # delay for drop to form
wiringpi.digitalWrite(solenoidpin,LOW)                 # close solenoid

sleep(t2)                                               # wait for the drop to fall some way

wiringpi.digitalWrite(solenoidpin,HIGH)                # second drop open solenoid
sleep(t3)                                               # second drop delay
wiringpi.digitalWrite(solenoidpin,LOW)                 # close solenoid

sleep(t4)                                               # wait for both drops to fall....

wiringpi.digitalWrite(shutterpin,HIGH)                 # open the shutter
sleep(t5)                                               # some delay for the shutter to fire
wiringpi.digitalWrite(shutterpin,LOW)                  # release the shutter
# note - people seem to think for bulb model, you need focus to be active first, then shutter