#!/usr/bin/python3
# license removed for brevity
import rospy
from custom_tutorials_msgs.msg import CustomMessage

def talker():
    
    pub = rospy.Publisher('chatter', CustomMessage, queue_size=10)
    rospy.init_node('custom_tutorials_talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    data = CustomMessage()
    while not rospy.is_shutdown():
        data.word = "hello world %s" % rospy.get_time()
        data.number = 10
        rospy.loginfo('data.word: %s' % data.word + '\n' 'data.number: %s' % str(data.number))
        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass