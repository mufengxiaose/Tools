#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 20:38 
# @Author : Carl
# @File : secPage.py

import tkinter as tk

class scePage(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("demo")
        self.window.geometry("600x500")

    # def screenShot(self):
    #     print("截图")
        shotbtn = tk.Button(self.window, text="截图")
        shotbtn.place(x=1, y=1, anchor='nw')
    # 取设备日志
        logBtn = tk.Button(self.window, text='拉日志')
        logBtn.place(x=1, y=30, anchor='nw')
