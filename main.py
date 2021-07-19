#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/12 17:33 
# @Author : Carl
# @File : main.py
import os, sys
base_file =  os.path.dirname(__file__)
sys.path.append(base_file)
from page import firstPage
from page import homePage
from page import demo

firstPage.window.mainloop()
# demo.demoPage()
# homePage.homePage()
# homePage.homePage().window.mainloop()
# demo.demoPage()