## Import relevant packages for raspberry pi
from machine import Pin,PWM
from time import sleep

# Choose output pin for PWM and "activate"
pin_PWM = Pin(3)
pwm = PWM(pin_PWM)

# Set frequency and duty cycle 
pwm.freq(100000)
pwm.duty_u16(32767)    ## duty cycle of 50%

# Turn on LED 1 
green_led = machine.Pin(25,Pin.OUT)
green_led.value(1)
sleep(10)
green_led.value(0)

# Turn on LED 2
red_led = machine.Pin(6,Pin.OUT)
red_led.value(1)
sleep(10)
red_led.value(0)
    
    

 

