import rospy
import numpy as np
import cv2

from sensor_msgs.msg import Image
from std_msgs.msg import String

class laneDetectionNODE:
    def __init__(self):
        # Init NODE
        rospy.init_node('laneDetectionNODE', anonymous=False)
        self.image_subscriber=rospy.Subscriber('automobile/image_raw', Image, self._process)
        self.command_publisher=rospy.Publisher('automobile/command', String, queue_size=1000)

    def _process(self, img):
        while not rospy.is_shutdown():
            # Xu li anh o day

            angle = None    
            steering_command = {"action":"2", "steerAngle": angle}
            self.command_publisher.publish(steering_command)