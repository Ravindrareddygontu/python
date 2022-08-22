from tkinter import *
import time
root = Tk()
root.title("Stopwatch")
root.config(bg="black")
width = 500
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
# take the window to center of screen
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
sec=00
hour=00
min=00
def Start():
    global timing, timer, hour, min, sec
    time.sleep(1)
    sec +=1
    if sec==60:
        sec=0
        min=min+1
    if min==60:
        min=0
        hour=hour+1
    timer.config(text=f'{hour}:{min}:{sec}')
    timing = timer.after(1,Start)
def Stop():
    global timing
    timer.after_cancel(timing)
def Reset():
    global sec, sec, min
    sec=00
    min=00
    hour=00
    timer.config(text=f'{hour}:{min}:{sec}')
    timer.after_cancel(timing)
    
def Exit():
    root.destroy()
    
Top = Frame(root, width=400)
Top.pack(side=TOP)
Bottom = Frame(root, width=400)
Bottom.pack(side=BOTTOM)

timer = Label(Top, font=("times new roman", 45), fg="white",bg="black")
timer.pack(fill=X, expand=NO, pady=10)
timer.config(text=f'{hour}:{min}:{sec}')

Startt = Button(Bottom, text='START',command=Start)
Startt.pack(side=LEFT,padx=2, pady=5)
    
Stopp = Button(Bottom, text='STOP',command=Stop)      
Stopp.pack(side=LEFT,padx=2, pady=5)

Resett = Button(Bottom, text='RESET', command=Reset)
Resett.pack(side=LEFT,padx=2, pady=5)

Exitt = Button(Bottom, text='CLOSE', command=Exit)
Exitt.pack(side=LEFT,padx=2, pady=5)
    
root.mainloop()
