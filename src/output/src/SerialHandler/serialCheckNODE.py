import rospy
import json
import time

from std_msgs.msg import String

class checkNODE:
    def __init__(self) -> None:
        rospy.init('checkNODE', anonymous=False)
        self.pub = rospy.Publisher('automobile/command', String, queue_size=1000)
        
    def _run(self):
        for i in range(-30, 30, 1):
            command = {"action": "2", "steerAngle": float(i)}
            command = json.dumps(command)
            self.pub.publish(command)
            time.sleep(0.01)

        for i in range(30, -30, -1):
            command = {"action": "2", "steerAngle": float(i)}
            command = json.dumps(command)
            self.pub.publish(command)
            time.sleep(0.01)

if __name__ =='__main__':
    checkNod = checkNODE()
    checkNod._run()