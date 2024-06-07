## Import relevant packages for raspberry pi
from machine import Pin,PWM
from time import sleep
import time

# Choose input pin for input and speaker and "activate"
pin_input = Pin(9,Pin.IN)
pin_speaker=PWM(Pin(10,Pin.OUT))

# Set alarm frequency
pin_speaker.freq(300)

# Check input pin value
print(pin_input.value())

t_timer = time.time()
pin_speaker.duty_u16(0)

while time.time()< t_timer + 195:
    
    if pin_input.value() == 1:    
        sleep(0.01)
        
    else:
            
        print('Your eggs are ready!!!')
        t_end = time.time() + 2
        while time.time() < t_end:
            
            pin_speaker.duty_u16(60000)
            sleep(0.3)
            pin_speaker.duty_u16(0)
            sleep(0.3)
            
       # with open("Egg_timer_GUI.py") as f:     ## Change path file - save to raspberry pi??
        #    exec(f.read())
        
pin_speaker.duty_u16(0)

