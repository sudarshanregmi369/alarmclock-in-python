from tkinter import *
import datetime
import winsound
import time 

def alarmclock(set_timer):
    while True:
        time.sleep(1)
        current_time  = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%D/%M/%Y")

        if now == current_time:
            print("it time to wake up ")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break
def actualtime():
    set_timer = f"{datetime.datetime.now().hour}:{datetime.datetime.now().minute}:{datetime.datetime.now().second}"
    alarmclock(set_timer)
actualtime()
# GUI
root = Tk()
root.title("Alarm clock")
root.geometry('600x600')

# adding a label to the root window
lbl = Label(root, text = " set the alarm")
lbl.grid()

def clicked():
    lbl.configure(text = "Alarm stopped")
 
# button widget with red color text
# inside
btn = Button(root, text = "Stop alarm" ,
             fg = "red", command=clicked)
# set Button grid
btn.grid(column=1, row=0)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
minute = StringVar()
second = StringVar()
#Time required to set the alarm clock:
hours = Entry(root, textvariable=hour,background="pink", width=15).place(x=110, y = 30 )
mins = Entry(root, textvariable=minute ,background="pink", width=15).place(x = 150, y = 30)
secs = Entry(root=root, textvariable=second, background="pink", width=15).place( x= 180, y =30)

#To take the time input by user:
submit = Button(root,text = "Set Alarm",fg="red",width = 10,command = actualtime).place(x =110,y=70)

root.mainloop()

       