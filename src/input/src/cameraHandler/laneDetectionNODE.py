import rospy
import numpy as np
import cv2
import time
import json

from sensor_msgs.msg import Image
from cv_bridge       import CvBridge
from std_msgs.msg import String

class laneDetectionNODE:
    def __init__(self):
        self.bridge = CvBridge()
        self.cv_image = np.zeros((640, 480))
        self.src_img = self.cv_image

        self.steer = 0.0
        # Init NODE
        rospy.init_node('laneDetectionNODE', anonymous=False)
        self.image_subscriber=rospy.Subscriber('automobile/image_raw', Image, self._process, queue_size = 1, buff_size = 2**24)
        self.command_publisher=rospy.Publisher('automobile/steering', String, queue_size=1000)

        rospy.spin()

    def _process(self, img):
        self.cv_image = self.bridge.imgmsg_to_cv2(img, "bgr8")
        self.src_img = self.cv_image
        src_img = self.cv_image.copy()
        src_img = cv2.resize(src_img,(640,480))
        
        # Image processing steps 

        
        steering = json.dumps({"steer": self.steer})
        self.command_publisher.publish(steering)