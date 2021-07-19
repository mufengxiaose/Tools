#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 20:56 
# @Author : Carl
# @File : secondPageFun.py

import os
import time
import datetime
time_stamp = '{0:%Y-%m-%d-%M-%H-%M}'.format(datetime.datetime.now())

class commonFun(object):
    def __init__(self):
        pass

    def runCmd(self, str):
        p = os.popen(str)
        return p.read()

    def screenShot(self):
        self.runCmd('adb shell screencap -p /sdcard/' + time_stamp + ".png")
        self.runCmd('adb pull sdcard/' + time_stamp + ".png" + "../data/pic")
        print("拉取截图完成")

    def pullLog(self):
        return self.runCmd('adb logcat -v threadtime' + ' ' + r'..\data\phonelog' + time_stamp + '.log')



if __name__ == '__main__':
    print(commonFun().runCmd('adb devices'))