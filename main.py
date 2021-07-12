#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/7/12 17:33 
# @Author : Carl
# @File : main.py
import os, sys
base_file =  os.path.dirname(__file__)
sys.path.append(base_file)
from page import firstPage

firstPage.window.mainloop()