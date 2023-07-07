import math
import tkinter as tk
from tkinter import *
from tkinter.font import Font
import sqlite3

def click(number):
    corrent = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(corrent)+ str(number))
    
def c():
    entry.delete(0, END)
    
'''def percent():
    second = entry.get()
    global f_num
    global math
    math = 'percent'
    f_num = float(second)
    entry.delete(0, END)'''
    
def square():
    second = entry.get()
    global f_num
    global math
    math ='square'
    f_num = float(second)
    entry.delete(0, END)   
    entry.insert(0, f_num**2)
        
def sqrt():
    second = entry.get()
    global f_num
    global math
    math = 'sqrt'
    f_num = float(second)
    entry.delete(0, END)   
    entry.insert(0, f_num**0.5)

def minus():
    second = entry.get()
    global f_num
    global math
    math = 'minus'
    f_num = int(second)
    entry.delete(0, END)
          
def plus():
    second = entry.get()
    global f_num
    global math
    math = 'plus'
    f_num = int(second)
    entry.delete(0, END)
    
def division():
    second = entry.get()
    global f_num
    global math
    math = 'division'
    f_num = int(second)
    entry.delete(0, END)
    
def multiplication():
    second = entry.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(second)
    entry.delete(0, END)
    
def backcpace():
    entry.delete(len(entry.get())-1, END)

def equal():
    first = entry.get()
    entry.delete(0,END)
    if math == 'plus':
        entry.insert(0, f_num + int(first))
    elif math == 'minus':
        entry.insert(0, f_num - int(first))
    elif math == 'division':
        if int(first) == 0:
            entry.insert(0, 'error')
        entry.insert(0, f_num / int(first))
    elif math == 'multiplication':
        entry.insert(0, f_num * int(first))
    if c_btn==True:
        entry.delete(0, END) 
    
    
calculator = tk.Tk()
calculator.title('Calculator')
calculator.geometry('320x410')
calculator.resizable(False, False)
calc_icon = PhotoImage(file='D:\python\git\calculator\calculator_icon.png')
calculator.iconphoto(True, calc_icon)
hist_icon = PhotoImage(file='D:\python\git\calculator\history_icon.png')
menu_icon = PhotoImage(file='D:\python\git\calculator\menu_icon.png')
bs_icon = PhotoImage(file='D:\python\git\calculator\Backspace_icon.png')
square_icon = PhotoImage(file='D:\python\git\calculator\square_icon.png')
one_div_icon = PhotoImage(file='D:\python\git\calculator\one_div_icon.png')
div_icon = PhotoImage(file='D:\python\git\calculator\div_icon.png')
multi_icon = PhotoImage(file='D:\python\git\calculator\multi_icon.png')
    
entry = tk.Entry(calculator, justify="right", font= ('verdana', 34 ), textvariable= BOTTOM)
entry.place(x= 4, y= 40, width=312, height=54,)

simple_lbl = Label(calculator, text='Обычный', font=('verdana',14)).place(x=40, y=5, width= 105, height= 20)
history_lbl = Label(calculator, image=hist_icon,).place(x=277, y=0, width=48, height=40)
menu_lbl = Label(calculator, image=menu_icon,).place(x=0, y=0, width=38, height=30)
'''
mc_btn = Button(calculator, text= 'MC', font=('verdana', 8), state=ACTIVE).place(x=4, y=145, width=50, height=35)
mr_btn = Button(calculator, text= 'MR', font=('verdana', 8), state=ACTIVE).place(x=56, y=145, width=50, height=35)
m_pl_btn = Button(calculator, text= 'M+', font=('verdana', 8), state=ACTIVE).place(x=108, y=145, width=50, height=35)
m_mn_btn = Button(calculator, text= 'M-', font=('verdana', 8), state=ACTIVE).place(x=162, y=145, width=50, height=35)
ms_btn = Button(calculator, text= 'MS', font=('verdana', 8), state=ACTIVE).place(x=214, y=145, width=50, height=35)
m_sq_btn = Button(calculator, text= 'M^', font=('verdana', 8), state=ACTIVE).place(x=266, y=145, width=50, height=35)'''

sqrt_btn = Button(calculator, text= '√', font=('verdana', 12), state=ACTIVE, command= sqrt).place(x=4, y=97, width=154, height=50)
square_btn = Button(calculator, image= square_icon, font=('verdana', 12), state=ACTIVE, command= square).place(x=162, y=97, width=155, height=50)

c_btn = Button(calculator, text= 'C', font=('verdana', 12), state=ACTIVE, command= c).place(x=2, y=149, width=156, height=50)
bs_btn = Button(calculator, image= bs_icon, state=ACTIVE, command= backcpace).place(x=162, y=149, width=75, height=50)
div_btn = Button(calculator, image= div_icon, font=('verdana', 12), state=ACTIVE, command= division).place(x=242, y=149, width=75, height=50)

seven_btn = Button(calculator, text= '7', font=('verdana', 12), state=ACTIVE, command= lambda: click(7)).place(x=2, y=201, width=75, height=50)
eight_btn = Button(calculator, text= '8', font=('verdana', 12), state=ACTIVE, command= lambda: click(8)).place(x=82, y=201, width=75, height=50)
nine_btn = Button(calculator, text= '9', font=('verdana', 12), state=ACTIVE, command= lambda: click(9)).place(x=162, y=201, width=75, height=50)
multi_btn = Button(calculator, image= multi_icon, font=('verdana', 12), state=ACTIVE, command= multiplication).place(x=242, y=201, width=75, height=50)

four_btn = Button(calculator, text= '4', font=('verdana', 12), state=ACTIVE, command= lambda: click(4)).place(x=2, y=253, width=75, height=50)
five_btn = Button(calculator, text= '5', font=('verdana', 12), state=ACTIVE, command= lambda: click(5)).place(x=82, y=253, width=75, height=50)
six_btn = Button(calculator, text= '6', font=('verdana', 12), state=ACTIVE, command= lambda: click(6)).place(x=162, y=253, width=75, height=50)
min_btn = Button(calculator, text= '-', font=('verdana', 12), state=ACTIVE, command= minus).place(x=242, y=253, width=75, height=50)

one_btn = Button(calculator, text= '1', font=('verdana', 12), state=ACTIVE, command= lambda: click(1)).place(x=2, y=305, width=75, height=50)
two_btn = Button(calculator, text= '2', font=('verdana', 12), state=ACTIVE, command= lambda: click(2)).place(x=82, y=305, width=75, height=50)
three_btn = Button(calculator, text= '3', font=('verdana', 12), state=ACTIVE, command= lambda: click(3)).place(x=162, y=305, width=75, height=50)
plus_btn = Button(calculator, text= '+', font=('verdana', 12), command=plus).place(x=242, y=305, width=75, height=50)

zero_btn = Button(calculator, text= '0', font=('verdana', 12), state=ACTIVE, command= lambda: click(0)).place(x=2, y=357, width=155, height=50)
equal_btn = Button(calculator, text= '=', font=('verdana', 12), command= equal).place(x=162, y=357, width=155, height=50)

calculator.mainloop()