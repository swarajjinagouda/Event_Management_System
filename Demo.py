from tkinter import * #Imports Tkinter
import sys #Imports sys, used to end the program later

root=Tk() #Declares root as the tkinter main window
top = Toplevel() #Creates the toplevel window

entry1 = Entry(top) #Username entry
entry2 = Entry(top) #Password entry
button1 = Button(top, text="Login", command=lambda:command1()) #Login button
button2 = Button(top, text="Cancel", command=lambda:command2()) #Cancel button
label1 = Label(root, text="This is your main window and you can input anything you want here")

def command1():
    if entry1.get() == "user" and entry2.get() == "password": #Checks whether username and password are correct
        root.deiconify() #Unhides the root window
        top.destroy() #Removes the toplevel window

def command2():
    top.destroy() #Removes the toplevel window
    root.destroy() #Removes the hidden root window
    sys.exit() #Ends the script
entry1.pack() #These pack the elements, this includes the items for the main window
entry2.pack()
button1.pack()
button2.pack()
label1.pack()

root.withdraw() #This hides the main window, it's still present it just can't be seen or interacted with
root.mainloop() #Starts the event loop for the main window