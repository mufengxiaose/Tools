#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/12 17:35 
# @Author : Carl
# @File : firstPage.py
import tkinter
from utils.firstPageFun import *
window = tkinter.Tk()
window.title("adb工具")
window.geometry('1100x500+10+10') #页面大小

def deviceConnect():    #显示设备连接状态
    deviceText.delete(1.0, tkinter.END)
    deviceText.insert(1.0, getDevices())
label1 = tkinter.Label(window, text="设备状态展示", width=20, height=1, fg='blue', font='Helvetica -16')
label1.place(x=0, y=1, anchor='nw')
deviceText = tkinter.Text(window, width=20, height=1, fg='blue', font='Helvetica -16')
deviceText.place(x=100, y=1, anchor='nw')

#更新设备信息
updateBtn = tkinter.Button(window, text="查看设备", command=deviceConnect, bd=2, width=10, font='Helvetica -16')
updateBtn.place(x=200, y=1, anchor='nw')
#设置测服
testBtn = tkinter.Button(window, text="切换测服", bd=2, width=10, command=set_test, font='Helvetica -16')
testBtn.place(x=1, y=40, anchor='nw')
#设置beta
betaBtn = tkinter.Button(window, text="切换Beta", bd=2, width=10, command=set_beta, font='Helvetica -16')
betaBtn.place(x=140, y=40, anchor='nw')
#设置正服
proBtn = tkinter.Button(window, text="切换正服", bd=2, width=10, command=set_pro, font='Helvetica -16')
proBtn.place(x=280, y=40, anchor='nw')
#拉取设备日志
getLogBtn = tkinter.Button(window, text="设备日志", bd=2, width=10, command=get_log, font='Helvetica -16')
getLogBtn.place(x=420, y=40, anchor='nw')
#查看设备fdk
fdkBt = tkinter.Button(window, text="fdk版本号", bd=2, width=10,command=get_fkd_version, font='Helvetica -16')
fdkBt.place(x=1, y=80, anchor='nw')
fdkStatus = tkinter.StringVar()
fdkText = tkinter.Label(window, textvariable=fdkStatus, fg="blue", bd=2, width=50, font='Helvetica -16')
fdkText.place(x=100, y=80, anchor='nw')
#修改设备version
#给设备添加id
#显示设备id，key
IdBtn = tkinter.Button(window, text="获取设备Id", bd=2, width=10, command=get_id_key, font='Helvetica -16')
IdBtn.place(x=1, y=120, anchor='nw')
IdStatus =  tkinter.StringVar()
IdLable = tkinter.Label(window, textvariable=IdStatus, fg="blue", bd=2, width=50, font='Helvetica -16')
IdLable.place(x=100, y=120, anchor='nw')
# IdLable.event_add(tkinter.Text.get())

#重启设备
rebootBtn = tkinter.Button(window, text='重启设备', bd=2, width=10, command=rebootDevice, font='Helvetica -16')
rebootBtn.place(x=1, y=160, anchor='nw')

#升级失败重置设备
updateFaileBtn = tkinter.Button(window, text='升级失败重置设备', bd=2, width=15, command=updateFaile, font='Helvetica -16')
updateFaileBtn.place(x=1, y=400, anchor='nw')