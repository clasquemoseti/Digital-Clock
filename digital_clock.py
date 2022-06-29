from tkinter import *
from tkinter import font,  ttk
import datetime
# import time


def quits(*args):
    root.destroy()


def clock_time():
    # et the current time
    time = datetime.datetime.now()
    # Format the time
    time = time.strftime("%H:%M:%S")
    txt.set(time)

    # Recursion; after every second, call clock_time
    root.after(1000, clock_time)


root = Tk()
root.attributes("-fullscreen", False)

# Configure the root window
root.configure(background="black", width=720, height=240)

# Bind keyboard key='q' to function 'quits'. when 'q' is pressed, the program terminates.
root.bind("q", quits)

root.after(1000, clock_time)

fnt = font.Font(family='Helvetica', size=120, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='white', background='black')
# Geometry of the label, relative to the root window
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
