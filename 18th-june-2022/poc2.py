from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
root = Tk()
root.geometry("700x500")
root.title("Age Calculator")
 
def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    months = today.month - birthDate.month
    days = today.day - birthDate.day
    Label(text=f"your age is {age}years, {months} months, {days} days").grid(row=6, column=1)
    
Label(text="Year").grid(row=2, column=0)
Label(text="Month").grid(row=3, column=0)
Label(text="Day").grid(row=4, column=0)
 
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()
 
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)
 
yearEntry.grid(row=2, column=1)
monthEntry.grid(row=3, column=1)
dayEntry.grid(row=4, column=1)

names = ("one","two","three","four")
button = Radiobutton(root, text='male', value=1)
button.place(x=100,y=150)
button = Radiobutton(root, text='female', value=2)
button.place(x=150, y=150)
mylist = Combobox(root, values=names)
mylist.place(x=170,y=250)
 
computeButton = Button(text="CalculateAge", command=calculateAge)
computeButton.grid(row=5, column=1, pady=10)

