#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/12 17:33 
# @Author : Carl
# @File : firstPageFun.py
import os, sys
import subprocess
import time
import datetime
import shutil
set_file = "/usr/lib"
time_stamp = '{0:%Y-%m-%d-%M-%H-%M}'.format(datetime.datetime.now())

#连接设备
def runCmd(str):
    p = os.popen(str)
    return p.read()
#设备连接状态
def getDevices():
    status = runCmd('adb devices').strip()
    print(status)
    if status == "List of devices attached":
        status = "当前无设备连接"
    else:
        status = status.replace("List of devices attached", "").strip()
    return status
def set_test():  #测服
    file = "adb push" + " " + "../Tools/so/beta/libwyzefdk.so" + " " + set_file
    setTest = runCmd(file)
    print(setTest)
    return setTest

def set_beta():  #beta切换
    file = "adb push" + " " + "../Tools/so/beta/libwyzefdk.so" + " " + set_file
    setBeat = runCmd(file)
    print(setBeat)
    return setBeat

def set_pro():  #正服切换
    file = "adb push" + " " + "../Tools/so/product/libwyzefdk.so" + " " + set_file
    setPro = runCmd(file)
    print(setPro)
    return setPro

def get_log():  #拉取设备日志
    file = "adb pull /mnt/UDISK/log" + " " + "../Tools/log/" + str(time_stamp)
    getLog = runCmd(file)
    # print(getLog)
    return getLog

def get_id_key(): #获取设备id、key
    file = "adb pull /mnt/SNN/ULI/factory" + " " + r"..\Tools\data\deviceID"
    getIdKey = runCmd(file)
    print(getIdKey)
    time.sleep(1)
    try:
        f_Id = open(r'..\Tools\data\deviceID\factory\device_id.txt')      #id
        # f_key = open(r'..\Tools\deviceIdKey\product_key.txt')     #key
        # delcet = shutil.rmtree(r'..\Tools\deviceIdKey\factory')
        # print(f_Id.read())
        return f_Id.read()
    except Exception as e:
        return "获取失败，请确认设备是否连接"
def get_fkd_version():  #获取设备fdk版本
    file = 'adb pull /mnt/UDISK/andon/logFdk/FDKVersion' + ' ' + r'..\Tools\data\fdkVersion'
    p = runCmd(file)
    print(p)
    time.sleep(1)
    try:
        f = open(r'..\Tools\data\fdkVersion\FDKVersion', 'r')
        # print(f.read())
        # delect = os.remove(r'..\Tools\version\FDKVersion')
        return f.read()
    except Exception as e:
        return "获取失败，请重试"

def set_id():
    pass

def set_version():
    pass

def rebootDevice():  #定义重启
    return runCmd('adb reboot')

def updateFaile():  #设备升级失败修复
    cmds = b"root\n@3I#sc$RD%xm^2S&\ntouch \mnt\UDISK\miss-upgrade/test.txt\nexit"
    p = subprocess.Popen('adb shell', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.communicate(cmds)
    print(p)
    return p, subprocess.Popen('adb reboot')

def rmFile():
    pass

# def search(root, target):
#     items = os.listdir(root)
#     for item in items:
#         path = os.path.join(root, item)
#         if os.path.isdir(path):
#             print('[-]', path)
#             search(path, target)
#         elif path.split('/')[-1] == target:
#             print('[+]', path)
#         else:
#             print('[!]', path)
#
# if __name__ == '__main__':
#     search('E:\code\Tools\data', '')