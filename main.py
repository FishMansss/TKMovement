import tkinter, math, time, os
from tkinter import *
root = Tk()
root.geometry("800x600")

w=800
h=600
x = w//2
y = h//2

can=Canvas(root,width=w, height=h, bg='white')
can.pack()

player=can.create_oval(x,y,x+10,y+10, outline="red")

