#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/18 22:14 
# @Author : Carl
# @File : demo.py
import tkinter as tk
from page import homePage

class demoPage(object):
    def demoBtn(self):
        btn = tk.Button(homePage.homePage(), text='demo')
        btn.place(x=1, y=1, anchor='nw')
