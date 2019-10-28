from jetcam.csi_camera import CSICamera
import cv2
import time
from jetbot import Robot
import logging
# from threading import Thread
import threading

# from jetcam.usb_camera import USBCamera

robot = Robot()
camera = CSICamera(width=224, height=224)
# camera = USBCamera(width=224, height=224)

camera.running = True

# def thread_function(name):
#     print("capturing")
#     cv2.imwrite("dataset/{0}-{1}.jpg".format("A", time.time()), camera.value)
#     print("done")
#     logging.info("Thread %s: starting", name)
#     time.sleep(.2)

# x = threading.Thread(target=thread_function, args=(100,))
# x.start()
#

i = 0;
while True:
    print("capturing")
    cv2.imwrite("dataset/{0}-{1}.jpg".format("A", time.time()), camera.value)
    time.sleep(1)
    print("done")
