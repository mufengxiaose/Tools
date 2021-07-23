#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk
import csv
def get_idKey(col):
    with open('../data/idkey.csv', 'r') as f:
        reader = csv.reader(f)
        data_list = []
        for i in reader:
            data_list.append(i[col])
    return data_list
            

if __name__ == '__main__':
    window = tk.Tk()
    window.title("demo")
    window.geometry('600x500')
    
    setIdlabel = tk.Label(window, text='id', bd=2, font='Helvetica -16').grid(column=0, row=0, sticky='E')

    setIdNum = tk.StringVar()
    setIdText = ttk.Combobox(window, textvariable=setIdNum, state='readonly', width=30)
    setIdText['value'] = get_idKey(col=0)
    setIdText.grid(row=0, column=1)

    setBtn = tk.Button(window, text='确认', bd=2, font='Helvetica -16').grid(column=1, row=2)

    window.mainloop()