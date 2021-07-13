from utility import *
import time
import os


ut = Utility()
while True:
    try:
        os.system("sudo pkill -9 libgpiod_pulsei")
        ut.geather_info()
        print("Data gethered")
        time.sleep(WAIT_TIME)
    except:
        pass