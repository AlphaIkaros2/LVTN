import numpy as np
import cv2
import json

import rospy
from std_msgs.msg import String

class actionNODE:
    def __init__(self):
        # Actuators variable
        self.steer = 0.0
        self.speed = 30.0

        self.pre_speed = self.speed
        self.pre_speed_smooth = 25
        
        # Signs tasks
        self.signs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Data container
        # Distance + imu task variable
        self.d1 = 0.0
        self.d2 = 0.0
        self.d3 = 0.0
        self.roll  = 0.0
        self.pitch = 0.0
        self.yaw   = 0.0

        # GPS pixels
        self.gps_x = 0.0
        self.gps_y = 0.0

        # Status
        self.pause = False

        # Init NODE
        rospy.init('actionNODE', anonymous=False)

        # Publisher
        self.command_publisher = rospy.Publisher('/automobile/command', String, queue_size=1000)

        # Subscribers
        self.sensor_data_subscriber = rospy.Subscriber('/automobile/data', String, self.process_data_callback, queue_size = 1)
        self.gps_subscriber = rospy.Subscriber('/automobile/gps', String, self.process_gps_callback, queue_size = 1)
        self.detection_subscriber = rospy.Subscriber('/automobile/detection', String, self.process_detection_callback, queue_size = 1)
        self.steer_subscriber = rospy.Subscriber('/automobile/steering', String, self.steer_callback, queue_size = 1)
        self.status_subscriber = rospy.Subscriber('/automobile/status', String, self.status_callback, queue_size = 1)

        rospy.spin()

    def status_callback(self, status_msg):
        status_data = json.loads(status_msg.data)
        self.status = status_data['status']
        

    def process_data_callback(self, data_msg):
        data = json.loads(data_msg.data)
        self.d1 = data['d1']
        self.d2 = data['d2']
        self.d3 = data['d3']
        self.roll  = data['roll']
        self.pitch = data['pitch']
        self.yaw   = data['yaw']



    def process_gps_callback(self, gps_msg):
        data = json.loads(gps_msg.data)
        self.gps_x = data['x']
        self.gps_y = data['y']

    def process_detection_callback(self, msg):
        data = json.loads(msg.data)
        self.signs = data['list_task']

    def steer_callback(self, steer):
        data = json.loads(steer.data)
        self.steer = data['steer']

    def _run_actions(self):
        while not self.pause:
            # Check data for actions

            # Carry out actions by sending commands
            pass
             