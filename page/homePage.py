#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 21:48 
# @Author : Carl
# @File : homePage.py
import tkinter as tk
from tkinter import ttk
# from tkinter import messagebox
# import csv
from utils.firstPageFun import *

window = tk.Tk()
window.title("测试工具")
window.geometry('1000x600+10+10')

tabControl = ttk.Notebook() #导航栏
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='固件')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='手机')
tabControl.pack(expand=1, fill='both')

"""固件部分"""
def deviceConnect():#显示设备连接状态
    deviceText.delete(1.0, tk.END)
    deviceText.insert(1.0, getDevices())
    # deviceText.insert(1.0, fun)
def deviceID(): #driverid展示
    IdText.delete(1.0, tk.END)
    IdText.insert(1.0, get_id_key())

def deviceFDK(): #fkd版本号展示
    fdkText.delete(1.0, tk.END)
    fdkText.insert(1.0, get_fkd_version())
#固件frame
tab1_frame1 = ttk.LabelFrame(tab1, text=" 设备状态 ")
tab1_frame1.grid(column=0, row=0, sticky='NW', padx=8, pady=4)
tab1_frame2 = ttk.LabelFrame(tab1, text=' 切换请求服务 ')
tab1_frame2.grid(column=0, row=1, sticky='W', padx=8, pady=4)
tab1_frame3 = ttk.LabelFrame(tab1, text="设备日志")
tab1_frame3.grid(column=0, row=2, sticky='NW', padx=8, pady=4)
tab1_frame4 = ttk.LabelFrame(tab1, text=" 设备fdk信息 ")
tab1_frame4.grid(column=0, row=3, sticky='NW', padx=8, pady=4)
tab1_frame5 = ttk.LabelFrame(tab1, text=" 设备fdk信息 ")
tab1_frame5.grid(column=0, row=4, sticky='NW', padx=8, pady=4)
tab1_frame6 = ttk.LabelFrame(tab1, text=" 重启、升级重置 ")
tab1_frame6.grid(column=0, row=5, sticky='NW', padx=8, pady=4)
tab1_frame7 = ttk.LabelFrame(tab1, text=" 添加设备id_key ")
tab1_frame7.grid(column=0, row=6, sticky='W', padx=8, pady=4)

label_1 = ttk.Label(tab1_frame1, text="设备名称")
label_1.grid(column=0, row=0, sticky='W')
deviceText = tk.Text(tab1_frame1, width=30, height=1.4, bd=2, fg='blue', font='Helvetica -16')
deviceText.grid(column=1, row=0, sticky='W')
deviceConnect()

updateBtn = tk.Button(tab1_frame1, text="更新连接状态", command=deviceConnect, bd=2, width=12, font='Helvetica -16')      #更新状态
updateBtn.grid(column=2, row=0, sticky='W')
#服务器切换
testBtn = tk.Button(tab1_frame2, text="切换测服", bd=2, width=10, command=set_test, font='Helvetica -16')     #设置测服
testBtn.grid(column=1, row=0, sticky='W')

betaBtn = tk.Button(tab1_frame2, text="切换Beta", bd=2, width=10, command=set_beta, font='Helvetica -16')   #设置beta
betaBtn.grid(column=2, row=0, sticky='W')

proBtn = tk.Button(tab1_frame2, text="切换正服", bd=2, width=10, command=set_pro, font='Helvetica -16')   #设置正服
proBtn.grid(column=3, row=0, sticky='W')

getLogBtn = tk.Button(tab1_frame3, text="获取设备日志", bd=2, width=12, command=get_log, font='Helvetica -16')    #拉取设备日志
getLogBtn.grid(column=0, row=0, sticky='W')
fileLabel = tk.Label(tab1_frame3, text="日志存放路径").grid(column=1, row=1, sticky='W')
getLogFile = tk.Text(tab1_frame3, fg="blue", bd=2, width=80, height=1, font='Helvetica -16')  #查看设备fdk
getLogFile.grid(column=0, row=1, sticky='W')

fdkText = tk.Text(tab1_frame4, fg="blue", bd=2, width=50, height=1, font='Helvetica -16')  #查看设备fdk
fdkText.grid(column=1, row=0, sticky='W')
fdkBt = tk.Button(tab1_frame4, text="fdk版本号", bd=2, width=10, command=deviceFDK, font='Helvetica -16')
fdkBt.grid(column=0, row=0, sticky='E')

IdBtn = tk.Button(tab1_frame5, text="获取设备Id", bd=2, width=10, command=deviceID, font='Helvetica -16')  #显示设备id，key
IdBtn.grid(column=0, row=0, sticky='E')
IdText = tk.Text(tab1_frame5, width=50, height=1, fg='blue', font='Helvetica -16')
IdText.grid(column=1, row=0, sticky='E')

rebootBtn = tk.Button(tab1_frame6, text='重启设备', bd=2, width=10, command=rebootDevice, font='Helvetica -16')   #重启设备
rebootBtn.grid(column=0, row=0, sticky='E')
updateFaileBtn = tk.Button(tab1_frame6, text='升级失败重置设备', bd=2, width=15, command=updateFaile, font='Helvetica -16')   #升级失败重置设备
updateFaileBtn.grid(column=1, row=0, sticky='E')

#设置id，key
def choose(*args):
    id = setIdText.get()
    with open(r'../data\setId\device_id.txt', 'w+') as f:
        f.write(id)
    print('id is: ' + id)
    reader = csv.reader(open(r'../data/idkey.csv', 'r'))
    for row in reader:
        if row[0] == id:
            with open(r'../data/setId/product_key.txt', 'w+') as f:
                f.write(row[1])
            print('key is:' + row[1])

setIdlabel = tk.Label(tab1_frame7, text='id', bd=2, font='Helvetica -16').grid(column=0, row=0, sticky='E')
setIdNum = tk.StringVar()
setIdText = ttk.Combobox(tab1_frame7, textvariable=setIdNum, state='readonly', width=30)
setIdText['value'] = get_idKey()
setIdText.bind('<<ComboboxSelected>>', choose)
setIdText.grid(row=0, column=1)

setBtn = tk.Button(tab1_frame7, text='确认', bd=2, font='Helvetica -16', command=set_id).grid(column=1, row=2)
#
# """手机部分"""



if __name__ == '__main__':
    window.mainloop()
