import numpy as np
import cv2

import rospy
from std_msgs.msg import String

class actionNODE:
    def __init__(self):
        # Data container
        self.data = ""
        self.gps = ""
        self.object_class = ""

        # Init NODE
        rospy.init('actionNODE', anonymous=False)
        self.sensor_data_subscriber = rospy.Subscriber('/automobile/data', String, self.process_data)
        self.gps_subscriber = rospy.Subscriber('/automobile/gps', String, self.process_gps)
        self.detection_subscriber = rospy.Subscriber('/automobile/detection', String, self.process_detection)

    def process_data(self, data):
        pass

    def process_gps(self, gps):
        pass

    def process_detection(self, msg):
        pass

    def _run_actions(self):
        while not rospy.is_shutdown():
            # Check data for actions

            # Carry out actions by sending commands

             