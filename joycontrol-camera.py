import warnings
warnings.filterwarnings("ignore")
from os import system, name

"""Simple example showing how to get gamepad events."""

#from __future__ import print_function 
from inputs import get_gamepad
from jetbot import Robot
import time
import sys

import numpy as np

robot = Robot()

motor_left_value = 0
motor_right_value = 0

y_val = 0;
x_val = 0;

print("Jetbot Started....")

import threading
def thread_function(name):
    while True:
        #if y_val > 0:
        #    print("................", y_val)
        #else:
        #    print("................" )
        #print(x_val)
        #if y_val < 0:
        #    print("................", y_val)
        #else:
        #    print("................" )
        motor_r = .3*y_val - .15*x_val
        motor_l = .3*y_val + .15*x_val 
        
        robot.left_motor.value = motor_l
        robot.right_motor.value = motor_r

x = threading.Thread(target=thread_function, args=(1,))
x.start()

def throttle(state):
    global y_val
    global motor_left_value, motor_right_value

    y_val = np.interp(state, [0, 255], [0.8, -0.8])

    
    #motor_left_value = out
    #motor_right_value = out
    #print('motor forward', out)


def steering(state):
    global x_val
    global left_factor, right_factor
    global motor_left_value, motor_right_value
    x_val = np.interp(state, [0, 255], [-.8, .8])
    
    #out = x_val 
    #out = np.interp(state, [0, 256], [, -1])
    #print('Z', state)

event_lut = {
    'ABS_RZ' : throttle,
    'ABS_Z' : steering,
}

#    'BTN_MODE': reset,
#    'BTN_START' : hello,
#    'BTN_NORTH' : lambda z: wave(z, 'right'),
#    'BTN_SOUTH' : celebrate,
#    'BTN_EAST' : circledance,
#    'BTN_WEST' : lambda z: wave(z, 'left'), #    'BTN_TR' : kick_right,
#    'BTN_TL' : kick_left,
#    'BTN_THUMBR' : kick_right,
#    'BTN_THUMBL' : kick_left,
#    'ABS_X' : turn,
#    'ABS_Y' : lambda x: walk(x, 23000),
#    'ABS_RX' : eyes,
#    'ABS_RY' : None, #lean,
#    'ABS_HAT0X': sidestep,
#    'ABS_HAT0Y': lambda x: walk(x, 0.5),

def main():
    events = get_gamepad()
    for event in events: 
        #print(event.ev_type, event.code, event.state)
        call = event_lut.get(event.code)
        if callable(call):
            call(event.state)
    

if __name__ == "__main__":
    #pads = inputs.devices.gamepads
    #if len(pads) == 0:
    #    raise Exception("{}Couldn't find any Gamepads!{}".format(fg('red'), attr('reset')))
    try:
        while True:
            main()
#             event_loop(inputs.get_gamepad())
    except KeyboardInterrupt:
        x.stop()
        print("Bye!")
        sys.exit()