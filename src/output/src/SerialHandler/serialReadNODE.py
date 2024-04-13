import serial
from messageconverter import MessageConverter
import json

import rospy 
from std_msgs.msg import String

class serialReadNODE:
    def __init__(self):
        # Specify COM port to receive data from ESP32
        devFile = '/dev/ttyUSB0'
        logFile = 'historyFile.txt'

        # Init COM
        self.serialCom = serial.Serial(devFile,19200,timeout=0.1)
        self.serialCom.flushInput()
        self.serialCom.flushOutput() 

        rospy.init_node('serialReadNODE', anonymous=False)
        self.data_publisher = rospy.Publisher('automobile/data', String, queue_size=1000)

    # ===================================== RUN ==========================================
    def run(self):
        """Apply the initializing methods and start the threads
        """
        rospy.loginfo("starting serialNODE")
        self._read()

    def _read(self):
        """ It's represent the reading activity on the the serial.
        """
        while not rospy.is_shutdown():
            read_line=self.serialCom.readline()
            read_line=(read_line.decode('ascii'))
            try:
                sensor_data=read_line.split("+")
                published_data = json.dumps({
                    "d1": sensor_data[0],
                    "d2": sensor_data[1],
                    "d3": sensor_data[2],
                    "roll": sensor_data[3],
                    "pitch": sensor_data[4],
                    "yaw": sensor_data[5]
                })
                self.data_publisher.publish(published_data)
            except UnicodeDecodeError:
                pass    

if __name__ == '__main__':
    serReadNode = serialReadNODE()
    serReadNode.run()