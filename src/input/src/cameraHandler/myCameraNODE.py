import numpy as np
from picamera2 import PiCamera2
import time
import cv2

import rospy

from cv_bridge       import CvBridge
from sensor_msgs.msg import Image

class myCameraNODE:
    def __init__(self):
        rospy.init('myCameraNODE', anonymous=False)

        self.image_publisher = rospy.Publisher("/automobile/image_raw", Image, queue_size=1)
        self.bridge = CvBridge()    
        self.camera = PiCamera2()

    def _init_camera(self):
        config = self.camera.create_preview_configuration(
            buffer_count=1,
            queue=False,
            main={"format": "XBGR8888", "size": (640, 480)},
        )
        self.camera.configure(config)
        self.camera.start()

    def _run(self):
        self._init_camera()
        while not rospy.is_shutdown():
            request = self.camera.capture_array("main")
            try:
                imageObject = self.bridge.cv2_to_imgmsg(request, "bgr8")
                self.image_publisher.publish(imageObject)
            except CvBridgeError as e:
                    print(e)
            cv2.imshow('frame', request)
            cv2.waitKey(1)
            
if __name__ == '__main__':
    camNod = myCameraNODE()
    camNod._run()

