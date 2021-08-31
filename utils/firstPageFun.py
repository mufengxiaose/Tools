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




set_file = "/usr/lib"
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
    elif "offline" in status:
        subprocess.Popen('adb kill-server')
        subprocess.Popen('adb devices')
    else:
        status = status.replace("List of devices attached", "").strip()
    return status

def get_log():  #拉取设备日志
    file_path = os.getcwd()
    test_file = file_path + r'\firmware_log'
    if os.path.exists(test_file): #判断文件路径是否存在，不存在则创建
        print('exist')
    else:
        os.mkdir(test_file)
    print("获取设备日志按钮")
    stime = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    file = "adb pull /mnt/UDISK/log" + " " + test_file + '/' + stime + '.log'
    runCmd(file)
    # file1 = os.path.dirname(os.path.dirname(__file__)) + '/log'
    lists = os.listdir(test_file)
    lists.sort(key=lambda fn: os.path.getmtime(test_file + '/' + fn))
    file_new = os.path.join(test_file, lists[-1])
    print(file_new)
    return file_new

def get_id_key(): #获取设备id、key
    file_path = os.getcwd()
    test_file = file_path + r'\id'
    if os.path.exists(test_file): #判断文件路径是否存在，不存在则创建
        print('exist')
    else:
        os.mkdir(test_file)
    file = "adb pull /mnt/SNN/ULI/factory" + " " + test_file
    runCmd(file)
    print("点击获取设备id按钮")
    try:
        deviceId = open(test_file + r'/factory/device_id.txt', 'r')      #id
        # file = 'data/deviceID/factory/device_id.txt'
        rm_file = test_file + r'/factory/device_id.txt'
        return deviceId.read(), deviceId.close(), os.remove(rm_file)
        # return deviceKey.read(), deviceKey.close()
    except Exception as e:
        return "获取失败，设备可能没有id，请设置id"
def get_fkd_version():  #获取设备fdk版本
    file_path = os.getcwd()
    test_file = file_path + r'\fdk'
    if os.path.exists(test_file): #判断文件路径是否存在，不存在则创建
        print('exist')
    else:
        os.mkdir(test_file)
    adb_pull = 'adb pull /mnt/UDISK/andon/logFdk/FDKVersion' + ' ' + test_file
    runCmd(adb_pull)
    print("获取设备fdk版本")
    # time.sleep(1)
    try:
        f = open(test_file + r'\FDKVersion', 'r')
        print(test_file + r'\FDKVersion')
        # delect = os.remove(r'..\Tools\version\FDKVersion')
        return f.read(), f.close(), os.remove(test_file + r'\FDKVersion')
    except Exception as e:
        return "获取失败，请重试"

def set_id(*args):      #给设备添加id，key
    # messagebox.showinfo('设置id', '稍等10秒，设置id中')
    print(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    file = '/mnt/SNN/ULI/factory'
    cmds = b"root\n\n@3I#sc$RD%xm^2S&\nmkdir -p /mnt/SNN/ULI/factory\n"
    p = subprocess.Popen('adb shell', stdin=subprocess.PIPE)
    time.sleep(0.1)
    p.communicate(cmds)
    p.kill()
    # p.wait()

    # deviceId = subprocess.Popen('adb push ..\Tools\device_id.txt' + ' ' + file)
    # deviceKye = subprocess.Popen('adb push ..\Tools\product_key.txt' + ' ' + file)
    print(datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    # return deviceId, deviceKye

def set_version():
    pass

def rebootDevice():  #定义重启
    print("重启设备按钮")
    return runCmd('adb reboot')

def updateFaile():  #设备升级失败修复
    print("设备升级失败按钮")
    # cmds = b"root\n@3I#sc$RD%xm^2S&\ntouch /mnt/UDISK/miss-upgrade/test.txt\nexit"
    # p = subprocess.Popen('adb shell', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    # p.communicate(cmds)
    # return p, subprocess.Popen('adb reboot')
    cmds = [
        "root",
        "@3I#sc$RD%xm^2S&",
        "touch /mnt/UDISK/miss-upgrade/test.txt",
        "exit"
    ]
    obj = subprocess.Popen("adb shell", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    info = obj.communicate(("\n".join(cmds) + "\n").encode("utf-8"))
    for item in info:
        if item:
            print(item.decode('gbk'))

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
    # get_log()
    get_fkd_version()