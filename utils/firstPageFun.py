#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/12 17:33 
# @Author : Carl
# @File : firstPageFun.py
import os, sys
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
    print("设备名称" + status)
    if status == "List of devices attached":
        status = "当前无设备连接"
    else:
        status = status.replace("List of devices attached", "").strip()
    return status
def set_test():  #测服
    file = "adb push" + " " + "../Tools/so/test/libwyzefdk.so" + " " + set_file
    setTest = runCmd(file)
    print("测服按钮")
    return setTest

def set_beta():  #beta切换
    file = "adb push" + " " + "../Tools/so/beta/libwyzefdk.so" + " " + set_file
    setBeat = runCmd(file)
    print("beta按钮")
    return setBeat

def set_pro():  #正服切换
    file = "adb push" + " " + "../Tools/so/product/libwyzefdk.so" + " " + set_file
    setPro = runCmd(file)
    print("正服按钮")
    return setPro

def get_log():  #拉取设备日志
    print("获取设备日志按钮")
    file = "adb pull /mnt/UDISK/log" + " " + "../Tools/log/" + str(time_stamp) + '.log'
    runCmd(file)
    f = os.path.abspath('../log')
    lists = os.listdir(f)
    lists.sort(key=lambda fn:os.path.getmtime(f + '/' + fn))
    file_new = os.path.join(f, lists[-1])
    print(file_new)
    return file_new

def get_id_key(): #获取设备id、key
    file = "adb pull /mnt/SNN/ULI/factory" + " " + r"..\Tools\data\deviceID"
    runCmd(file)
    print("点击获取设备id按钮")
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
    runCmd(file)
    print("获取设备fdk版本")
    # time.sleep(1)
    try:
        f = open(r'..\Tools\data\fdkVersion', 'r')
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
    print("重启设备按钮")
    return runCmd('adb reboot')

def updateFaile():  #设备升级失败修复
    print("设备升级失败按钮")
    cmds = b"root\n@3I#sc$RD%xm^2S&\ntouch /mnt/UDISK/miss-upgrade/test.txt\nexit"
    p = subprocess.Popen('adb shell', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    p.communicate(cmds)
    return p, subprocess.Popen('adb reboot')

def del_file(path, swith):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(swith):
                os.remove(os.path.join(root, name))
                print("Delete File: " + os.path.join(root, name))

def get_idKey():    #展示现有idkey.csv现有id
    print("展示所有未启用id")
    # with open('../data/idkey.csv', 'r') as f:
    with open('..\Tools\idkey.csv', 'r') as f:
        reader = csv.reader(f)
        data_list = []
        for i in reader:
            data_list.append(i[0])
    return data_list

if __name__ == '__main__':
    get_log()