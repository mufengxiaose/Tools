#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/12 17:33 
# @Author : Carl
# @File : firstPageFun.py
import os, sys
import subprocess
import time
import datetime
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
    file = "adb push" + " " + "../adbTools/so/beta/libwyzefdk.so" + " " + set_request_file
    setTest = runCmd(file)
    print(setTest)
    return setTest

def set_beta():  #beta切换
    file = "adb push" + " " + "../adbTools/so/beta/libwyzefdk.so" + " " + set_request_file
    setBeat = runCmd(file)
    print(setBeat)
    return setBeat

def set_pro():  #正服切换
    file = "adb push" + " " + "../adbTools/so/product/libwyzefdk.so" + " " + set_request_file
    setPro = runCmd(file)
    print(setPro)
    return setPro

def get_log():  #拉取设备日志
    file = "adb pull /mnt/UDISK/log" + " " + "../adbTools/log/" + str(time_stamp)
    getLog = runCmd(file)
    # print(getLog)
    return getLog

def get_id_key(): #获取设备id、key
    file = "adb pull /mnt/SNN/ULI/factory" + " " + "../adbTools/deviceIdKey"
    getIdKey = runCmd(file)
    # print(getIdKey)
    time.sleep(1)
    f_Id = open(r'..\adbTools\deviceIdKey\device_id.txt')
    # f_key = open(r'..\adbTools\deviceIdKey\product_key.txt')
    IdStatus.set(f_Id.read())
    f_Id.close()
    time.sleep(3)
    delcet = shutil.rmtree(r'..\adbTools\deviceIdKey\factory')
    return getIdKey, delcet

def get_fkd_version():  #获取设备fdk版本
    p = runCmd('adb pull /mnt/UDISK/andon/logFdk/FDKVersion' + ' ' + '../adbTools/version/')
    time.sleep(2)
    f = open(r'..\adbTools\version\FDKVersion', 'r')
    fdkStatus.set(f.read())
    f.close()
    time.sleep(3)
    delect = os.remove(r'..\adbTools\version\FDKVersion')
    return p, delect

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

