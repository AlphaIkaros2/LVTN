import serial
from messageconverter import MessageConverter
import json
import time

import rospy 
from std_msgs.msg import String

class serialWriteNODE:
    def __init__(self):
        # Specify COM port to write data to STM32 blue pill
        devFile = '/dev/ttyUSB1'

        # Init COM
        self.serialCom = serial.Serial(devFile,115200,timeout=0.1)
        self.serialCom.flushInput()
        self.serialCom.flushOutput() 

        # message converted init
        self.messageConverter = MessageConverter()

        rospy.init_node('serialWriteNODE', anonymous=False)
        self.data_publisher = rospy.Subscriber('automobile/command', String, self._write)
        
        # Keeps the node alive 
        rospy.spin()

    def _write(self, msg):
        """ Represents the writing activity on the the serial.
        """
        command = json.loads(msg.data)
        # Unpacking the dictionary into action and values
        command_msg = self.messageConverter.get_command(**command)
        self.serialCom.write(command_msg.encode('ascii'))
        self.historyFile.write(command_msg)