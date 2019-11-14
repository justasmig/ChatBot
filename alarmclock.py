import time
from tkinter import *
import winsound
import math


def tick():
    time_string = time.strftime("%H:%M:%S")
    clock.config(text=time_string)
    clock.after(200, tick)


root = Tk()
clock = Label(root, font=("times", 40, "bold"), bg="black", fg="red")
clock.grid(row=0, column=1)
tick()


def countdown(count):
    seconds = math.floor(count % 60)
    minutes = math.floor((count / 60) % 60)
    hours = math.floor((count / 3600))
    label['text'] = "Hours: " + str(hours) + " Minutes:  " + str(minutes) + " Seconds: " + str(seconds)

    if count >= 0:
        top.after(1000, countdown, count - 1)
    else:
        for x in range(3):
            winsound.Beep(1000,
                          1000)  # this could be changed from beep into a ringtone with a different command but i settled for the beep
        label['text'] = "rise and shine"


def updateButton():
    hour, minute, sec = hoursE.get(), minuteE.get(), secondE.get()
    if hour.isdigit() and minute.isdigit() and sec.isdigit():
        time = int(hour) * 3600 + int(minute) * 60 + int(sec)
        countdown(time)


top = Tk()
top.geometry("250x150")
hoursT = Label(top, text="Hours:")
hoursE = Entry(top)
minuteT = Label(top, text="Minutes:")
minuteE = Entry(top)
secondT = Label(top, text="Seconds:")
secondE = Entry(top)
hoursT.grid(row=1, column=1)
hoursE.grid(row=1, column=2)
minuteT.grid(row=2, column=1)
minuteE.grid(row=2, column=2)
secondT.grid(row=3, column=1)
secondE.grid(row=3, column=2)
label = Label(top)
label.grid(row=5, column=2)

button = Button(top, text="Start Countdown", command=updateButton)
button.grid(row=4, column=2)

def runner():
    root.mainloop()
    top.mainloop()
