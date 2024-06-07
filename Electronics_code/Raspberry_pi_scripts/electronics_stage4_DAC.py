## Import relevant packages for raspberry pi
from machine import Pin,PWM
from time import sleep

# Choose output pin for PWM and "activate"
pin_PWM = Pin(3)
pwm = PWM(pin_PWM)

# Set frequency and duty cycle for RC circuit
pwm.freq(20000)
pwm.duty_u16(32767) 