import warnings
from jetcam.csi_camera import CSICamera

warnings.filterwarnings("ignore")
from os import system, name

"""Simple example showing how to get gamepad events."""

# from __future__ import print_function
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
        motor_r = .3 * y_val - .15 * x_val
        motor_l = .3 * y_val + .15 * x_val

        robot.left_motor.value = motor_l
        robot.right_motor.value = motor_r


x = threading.Thread(target=thread_function, args=(1,))
x.start()


def throttle(state):
    global y_val
    global motor_left_value, motor_right_value

    y_val = np.interp(state, [0, 255], [0.8, -0.8])

    # motor_left_value = out
    # motor_right_value = out
    # print('motor forward', out)


def steering(state):
    global x_val
    global left_factor, right_factor
    global motor_left_value, motor_right_value
    x_val = np.interp(state, [0, 255], [-.8, .8])

    # out = x_val
    # out = np.interp(state, [0, 256], [, -1])
    # print('Z', state)


event_lut = {
    'ABS_RZ': throttle,
    'ABS_Z': steering,
}


def main():
    events = get_gamepad()
    for event in events:
        print(event.ev_type, event.code, event.state)

        call = event_lut.get(event.code)
        if callable(call):
            call(event.state)


from capture import CaptureImage

if __name__ == "__main__":
    tt = CaptureImage()
    tt.start()
    # pads = inputs.devices.gamepads
    # if len(pads) == 0:
    #    raise Exception("{}Couldn't find any Gamepads!{}".format(fg('red'), attr('reset')))
    try:
        while True:
            main()
    #             event_loop(inputs.get_gamepad())
    except KeyboardInterrupt:
        x.stop()
        print("Bye!")
        sys.exit()
