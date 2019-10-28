import warnings
warnings.filterwarnings("ignore")
from os import system, name

from jetcam.csi_camera import CSICamera
import cv2
import time
from jetbot import Robot
import logging
#from threading import Thread
import threading
from inputs import get_gamepad
import sys
import numpy as np
# from jetcam.usb_camera import USBCamera

robot = Robot()
camera = CSICamera(width=224, height=224)
# camera = USBCamera(width=224, height=224)

camera.running = True

motor_left_value = 0
motor_right_value = 0

y_val = 0;
x_val = 0;

print("Jetbot Started....")

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
        
        print("capturing")
        cv2.imwrite("dataset-road/{0}-{1}.jpg".format("A", time.time()), camera.value)
        print("done")
        logging.info("Thread %s: starting", name)
        time.sleep(.2)
        
threads = threading.Thread(target=thread_function, args=(1,))
threads.start()
        
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


# def thread_function(name):
#     print("capturing")
#     cv2.imwrite("dataset-road/{0}-{1}.jpg".format("A", time.time()), camera.value)
#     print("done")
#     logging.info("Thread %s: starting", name)
#     time.sleep(1)
    
    
def main():
    events = get_gamepad()
    for event in events: 
        #print(event.ev_type, event.code, event.state)
        call = event_lut.get(event.code)
        if callable(call):
            call(event.state)
            
i = 0;
while True: 
    try:
        while True:
            main()
    except KeyboardInterrupt:
        x.stop()
        print("Bye!")
        sys.exit()

#     print("capturing")
#     cv2.imwrite("dataset-road/{0}-{1}.jpg".format("A", time.time()), camera.value)
#     time.sleep(1) 
#     print("done")
    