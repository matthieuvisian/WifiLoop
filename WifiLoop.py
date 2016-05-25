#!/usr/bin/python

import os
import time

Time = 10

while True:
    response = os.system("ping -c 1 -q www.google.com > NULL")
    if (response == 1):
        os.system("sudo ifdown wlan0")
        os.system("sudo ifup wlan0")
    time.sleep(Time)
