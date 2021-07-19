#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 21:48 
# @Author : Carl
# @File : homePage.py
import tkinter as tk
from page import demo

class homePage(object):
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("测试工具")
        self.window.geometry('1000x600+10+10')
        self.winMenu()
        # self.demoBtn()
        # self.window.mainloop()

    def winMenu(self):
        self.menu = tk.Menu(self.window)
        self.window['menu'] = self.menu
        self.menu.add_command(label='菜单')
        self.menu.add_command(label='手机工具')

    def demoBtn(self):
        btn = tk.Button(self.window, text='demo').pack()
#
# demo.demoPage()
# homePage()