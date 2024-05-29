

from tkinter import *
import os
from tkinter import filedialog
import cv2
import time

from tkinter import messagebox





def endprogram():
	print ("\nProgram terminated!")
	sys.exit()










def fulltraining():
    import detection as mm





















def main_account_screen():
    global main_screen
    main_screen = Tk()
    width = 600
    height = 600
    screen_width = main_screen.winfo_screenwidth()
    screen_height = main_screen.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    main_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))
    main_screen.resizable(0, 0)
    main_screen.title("Animal  Detection")

    Label(text="Animal  Detection", width="300", height="5", font=("Calibri", 16)).pack()


    Button(text="Start Camera", font=(
        'Verdana', 15), height="2", width="30", command=fulltraining, highlightcolor="black").pack(side=TOP)

    Label(text="").pack()


    Label(text="").pack()

    main_screen.mainloop()


main_account_screen()

