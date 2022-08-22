import random
from tkinter import *

def dicing():
    dice = ['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    num = random.choice(dice)
    label.config(text=f"{num}")
    label.pack()

root = Tk()
root.geometry("400x300")
label = Label(root,font=("Helvetica",160))
Button(root, text="Roll", foreground = "Blue",command=dicing).place(x=100,y=20)
