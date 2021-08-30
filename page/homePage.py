#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 21:48 
# @Author : Carl
# @File : homePage.py
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import *
from utils.firstPageFun import *
from tkinter import messagebox

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

def deviceID(): #driverid展示
    IdText.delete(1.0, tk.END)
    IdText.insert(1.0, get_id_key())

def deviceFDK(): #fkd版本号展示
    fdkText.delete(1.0, tk.END)
    fdkText.insert(1.0, get_fkd_version())

def log_file(): #定义日志获取路径
    getLogFile.delete(1.0, tk.END)
    getLogFile.insert(1.0, get_log())


# #设置id，key
# def choose(*args):
#     id = setIdText.get()
#     # with open(r'../data\setId\device_id.txt', 'w+') as f:
#     with open(r'..\Tools\device_id.txt', 'w+') as f:
#         f.write(id)
#     print('id is: ' + id)
#     # reader = csv.reader(open(r'../data/idkey.csv', 'r'))
#     reader = csv.reader(open(r'..\Tools\idkey.csv', 'r'))
#     for row in reader:
#         if row[0] == id:
#             # with open(r'../data/setId/product_key.txt', 'w+') as f:
#             with open(r'..\Tools\product_key.txt', 'w+') as f:
#                 f.write(row[1])
#             print('key is:' + row[1])


#固件frame
tab1_frame1 = ttk.LabelFrame(tab1, text=" 设备状态 ")
tab1_frame1.grid(column=0, row=0, sticky='NW', padx=8, pady=4)
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
tabl_frame_server = ttk.LabelFrame(tab1, text=" 切换请求服务 ")
tabl_frame_server.grid(column=0, row=1, sticky='W', padx=8, pady=4)

label_1 = ttk.Label(tab1_frame1, text="设备名称")
label_1.grid(column=0, row=0, sticky='W')
deviceText = tk.Text(tab1_frame1, width=30, height=1.4, bd=2, fg='blue', font='Helvetica -16')
deviceText.grid(column=1, row=0, sticky='W')
deviceConnect()

updateBtn = tk.Button(tab1_frame1, text="更新连接状态", command=deviceConnect, bd=2, width=12, font='Helvetica -16')      #更新状态
updateBtn.grid(column=2, row=0, sticky='W')

#获取日志
getLogBtn = tk.Button(tab1_frame3, text="获取设备日志", bd=2, width=12, command=log_file, font='Helvetica -16')
getLogBtn.grid(column=0, row=0, sticky='W')
fileLabel = tk.Label(tab1_frame3, text="日志存放路径").grid(column=1, row=1, sticky='W')
getLogFile = tk.Text(tab1_frame3, fg="blue", bd=2, width=60, height=1, font='Helvetica -16')
getLogFile.grid(column=0, row=1, sticky='W')
# 查看设备fdk
fdkText = tk.Text(tab1_frame4, fg="blue", bd=2, width=50, height=1, font='Helvetica -16')
fdkText.grid(column=1, row=0, sticky='W')
fdkBt = tk.Button(tab1_frame4, text="fdk版本号", bd=2, width=10, command=deviceFDK, font='Helvetica -16')
fdkBt.grid(column=0, row=0, sticky='E')
#显示设备id，key
IdBtn = tk.Button(tab1_frame5, text="获取设备Id", bd=2, width=10, command=deviceID, font='Helvetica -16')
IdBtn.grid(column=0, row=0, sticky='E')
IdText = tk.Text(tab1_frame5, width=50, height=1, fg='blue', font='Helvetica -16')
IdText.grid(column=1, row=0, sticky='E')
# 重启设备
rebootBtn = tk.Button(tab1_frame6, text='重启设备', bd=2, width=10, command=rebootDevice, font='Helvetica -16')
rebootBtn.grid(column=0, row=0, sticky='E')
# updateFaileBtn = tk.Button(tab1_frame6, text='升级失败重置设备', bd=2, width=15, command=updateFaile, font='Helvetica -16')   #升级失败重置设备
# updateFaileBtn.grid(column=1, row=0, sticky='E')
#固件设置id按钮部分
# setIdlabel = tk.Label(tab1_frame7, text='id', bd=2, font='Helvetica -16').grid(column=0, row=0, sticky='E')
# setIdNum = tk.StringVar()
# setIdText = ttk.Combobox(tab1_frame7, textvariable=setIdNum, state='readonly', width=30, value=get_idKey())
# setIdText.bind('<<ComboboxSelected>>', choose)
# setIdText.grid(row=0, column=1)
# setBtn = tk.Button(tab1_frame7, text='确认', bd=2, font='Helvetica -16', command=set_id).grid(column=1, row=2)



#设置请求服务
#请求服务文件导入、切换
def import_file():
    filepath = askopenfilename()
    print(filepath)
    entry_import.delete(0, tk.END)
    entry_import.insert(0, filepath)
def confirm_switch():
    file = entry_import.get()
    if str(file) == "选择文件路径...":
        messagebox.showinfo(message="请确认路径是否正确")
    else:
        p = 'adb push' + ' ' + str(file) + ' ' + '/usr/lib'
        return subprocess.Popen(p)


button_import = tk.Button(tabl_frame_server, text='导入文件', command=import_file)
button_import.grid(column=0, row=0, sticky='E')
entry_import = tk.Entry(tabl_frame_server, width=60, bd=2, font=("宋体", 10, 'bold'))
entry_import.grid(column=1, row=0, sticky='E')
entry_import.delete(0, tk.END)
entry_import.insert(0, '选择文件路径...')
filepath=StringVar()
button_confirm = tk.Button(tabl_frame_server, text='确认切换', command=confirm_switch)
button_confirm.grid(column=3, row=0, sticky='E')

# """手机部分"""





if __name__ == '__main__':
    pass
