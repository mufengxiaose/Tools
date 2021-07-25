#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/12 17:33 
# @Author : Carl
# @File : firstPageFun.py
import os, sys
base_file =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_file + '/data/setId')

sys.path.append(base_file)
import subprocess
import time
import csv
import datetime
# import shutil
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
    file = "adb push" + " " + "../Tools/so/test/libwyzefdk.so" + " " + set_file
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
    file = "adb pull /mnt/UDISK/log" + " " + "../Tools/log/" + str(time_stamp) + '.log'
    getLog = runCmd(file)
    # print(getLog)
    return getLog

def get_id_key(): #获取设备id、key
    file = "adb pull /mnt/SNN/ULI/factory" + " " + r"..\Tools\data\deviceID"
    getIdKey = runCmd(file)
    # print(getIdKey)
    # time.sleep(1)
    try:
        deviceId = open(r'data/deviceID/factory/device_id.txt', 'r')      #id
        # deviceKey = open(r'data/deviceID/factory/product_key.txt', 'r')     #key
        file = 'data/deviceID/factory/device_id.txt'
        return deviceId.read(), deviceId.close(), os.remove(file)
        # return deviceKey.read(), deviceKey.close()
    except Exception as e:
        return "获取失败，设备可能没有id，请设置id"
def get_fkd_version():  #获取设备fdk版本
    file = 'adb pull /mnt/UDISK/andon/logFdk/FDKVersion' + ' ' + r'..\Tools\data\fdkVersion'
    p = runCmd(file)
    print(p)
    # time.sleep(1)
    try:
        f = open(r'..\Tools\data\fdkVersion', 'r')
        # print(f.read())
        # delect = os.remove(r'..\Tools\version\FDKVersion')
        return f.read(), f.close(), os.remove(r'..\Tools\data\fdkVersion')
    except Exception as e:
        return "获取失败，请重试"

def set_id(*args):      #给设备添加id，key
    file = '/mnt/SNN/ULI/factory'
    cmds = b"root\n@3I#sc$RD%xm^2S&\nmkdir -p /mnt/SNN/ULI/factory"
    subprocess.Popen('adb shell', stdin=subprocess.PIPE, stdout=subprocess.PIPE).communicate(cmds)
    time.sleep(0.1)
    deviceId = subprocess.Popen('adb push ../data/setId/device_id.txt ' + file)
    deviceKye = subprocess.Popen('adb push ../E:\code\Tools\data\setId\product_key.txt' + file)
    return deviceId, deviceKye

def set_version():
    pass

def rebootDevice():  #定义重启
    return runCmd('adb reboot')

def updateFaile():  #设备升级失败修复
    cmds = b"root\n@3I#sc$RD%xm^2S&\ntouch /mnt/UDISK/miss-upgrade/test.txt\nexit"
    p = subprocess.Popen('adb shell', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.communicate(cmds)
    print(p)
    return p, subprocess.Popen('adb reboot')

def del_file(path, swith):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(swith):
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))

def get_idKey():    #展示现有idkey.csv现有id
    with open('../data/idkey.csv', 'r') as f:
        reader = csv.reader(f)
        data_list = []
        for i in reader:
            data_list.append(i[0])
    return data_list

if __name__ == '__main__':
    # search('E:\code\Tools\data', '')
    path = r'..Tools\data\deviceID'
    del_file(path, '.txt')