## Import relevant packages for raspberry pi
from machine import Pin,PWM
from time import sleep, sleep_us
import time as time

# Choose output pin for PWM and "activate"
pin_PWM = Pin(3)
pwm = PWM(pin_PWM)

# Set frequency and duty cycle for RC circuit
pwm.freq(10000)


sin_wave = [0.5, 0.5317, 0.5633, 0.5946, 0.6256, 0.656, 0.6858, 0.7149,
            0.7431, 0.7703, 0.7965, 0.8214, 0.845, 0.8673, 0.8881, 0.9073,
            0.9249, 0.9407, 0.9548, 0.9671, 0.9775, 0.9859, 0.9924, 0.9969,
            0.9994, 0.9999, 0.9984, 0.9949, 0.9894, 0.9819, 0.9725, 0.9612,
            0.948, 0.933, 0.9163, 0.8979, 0.8779, 0.8563, 0.8334, 0.8091,
            0.7835, 0.7568, 0.7291, 0.7005, 0.671, 0.6409, 0.6102, 0.579,
            0.5475, 0.5159, 0.4841, 0.4525, 0.421, 0.3898, 0.3591, 0.329,
            0.2995, 0.2709, 0.2432, 0.2165, 0.1909, 0.1666, 0.1437, 0.1221,
            0.1021, 0.0837, 0.067, 0.052, 0.0388, 0.0275, 0.0181, 0.0106,
            0.0051, 0.0016, 0.0001, 0.0006, 0.0031, 0.0076, 0.0141, 0.0225,
            0.0329, 0.0452, 0.0593, 0.0751, 0.0927, 0.1119, 0.1327, 0.155, 0.1786,
            0.2035, 0.2297, 0.2569, 0.2851, 0.3142, 0.344, 0.3744, 0.4054, 0.4367, 0.4683, 0.5]


def Sine_Wave(frequency):
    
    time = 1/frequency   # convert frequency to time
    time_delay = time/100  # calculate time delay
    time_delay_us = time_delay*1000000          # convert time delay from seconds to us
    print(time_delay_us)

    while True:        
        for i in sin_wave:  
                
            duty_cycle = 65535*(i)     
            pwm.duty_u16(int(duty_cycle))
            
            sleep_us(int(time_delay_us))
            
            
Sine_Wave(20)  

