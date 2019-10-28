import threading
import time
import cv2
from jetcam.csi_camera import CSICamera


class CaptureImage(threading.Thread):

    # Thread class with a _stop() method.
    # The thread itself has to check
    # regularly for the stopped() condition.

    def __init__(self, *args, **kwargs):
        super(CaptureImage, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
        self._camera = CSICamera(width=224, height=224)
        self._camera.running = True
        print("camera was init :)")

        # function using _stop function

    def stop(self):
        self._camera.running = False
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def run(self):
        while True:
            if self.stopped():
                return
            file = "dataset/{0}-{1}.jpg".format("A", time.time())
            cv2.imwrite(file, self._camera.value)
            time.sleep(1)

    # def capture(self, cls, len):
    #
    #     # cv2.imwrite("dataset/{0}-{1}.jpg".format("A", time.time()), camera.value)
    #     # cap = cv2.VideoCapture(0)
    #     # print("myfunc started")
    #     # for i in range(0, len):
    #     #     ret, frame = cap.read()
    #     #     cv2.imwrite("dataset/{0}/{1}.jpg".format(cls, time.time()), frame)
    #     #     print("saved")
