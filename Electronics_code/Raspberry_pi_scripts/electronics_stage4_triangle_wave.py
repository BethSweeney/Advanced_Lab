## Import relevant packages for raspberry pi
from machine import Pin,PWM
from time import sleep, sleep_us
import time as time

# Choose output pin for PWM and "activate"
pin_PWM = Pin(3)
pwm = PWM(pin_PWM)

# Set frequency and duty cycle for RC circuit
pwm.freq(20000)


# Triangle wave pwm percentage range
triangle_total =[ 0, 1, 2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 98, 97,
       96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82,
       81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65,
       64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48,
       47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31,
       30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14,
       13, 12, 11, 10,  9,  8,  7,  6,  5,  4,  3, 2]


  
def Triangle_Wave(frequency):
    
    time = 1/frequency   # convert frequency to time
    time_delay = time/200  # calculate time delay
    time_delay_us = time_delay*1000000          # convert time delay from seconds to us
    print(time_delay_us)

    while True:        
        for i in triangle_total:  
                
            duty_cycle = 65535*(int(i)/100)     
            pwm.duty_u16(int(duty_cycle))
            
            sleep_us(int(time_delay_us)-50)      ## - 50 to improve frequency accuracy
         
            
# Run function for specific frequency
Triangle_Wave(10)

    
