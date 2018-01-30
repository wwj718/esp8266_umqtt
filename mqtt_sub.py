#!/usr/bin/env python
# encoding: utf-8

import time
from simple_mqtt import MQTTClient

time.sleep(10) #还没有连接到wifi
# Publish test messages e.g. with:
# mosquitto_pub -t foo_topic -m hello

# Received messages from subscriptions will be delivered to this callback
server="mqtt.just4fun.site"
c = MQTTClient("umqtt_client", server)

def sub_cb(topic, msg):
    # 都是bytes
    print((topic, msg))
    # to exec
    c.publish(b"/test_pub_umqtt", b"I get it!",qos=1,retain=True)
    # pub i get it

def main():
    c.set_callback(sub_cb)
    c.connect()
    #c.subscribe(b"/test_umqtt")
    c.subscribe(b"/test_sub_umqtt",qos=1)
    while True:
        if True:
            # Blocking wait for message
            print("running...")
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            time.sleep(1)

    c.disconnect()

if __name__ == "__main__":
    main()
