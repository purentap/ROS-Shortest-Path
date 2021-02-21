#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!pip install keyboard
import rospy
#import keyboard
from std_msgs.msg import String

def keystrokes():
  pub = rospy.Publisher("keystroke", String, queue_size = 1) #declares this node is publishing to the keystroke topic. #queue size emin değilim
  rospy.init_node("key_input", anonymous = True) #initalize the node
  rate = rospy.Rate(10)
  while not rospy.is_shutdown():
    #try: 
    user_input = raw_input("Press enter to generate a random maze") 
    if not user_input: 
      message = "keystroke detected"
      rospy.loginfo(message) #message get printed to screen, get written to the Node's log file, and it gets written to rosout
      pub.publish(message) #publishes the string to the keystroke topic
#except:
#  pass
    rate.sleep()
    
if __name__ == '__main__':
  try:
    keystrokes()
  except rospy.ROSInterruptException:
    pass

"""

```
# Bu, kod olarak biçimlendirilmiştir
```

/usr/bin/env: ‘python\r’: No such file or directory
"""
