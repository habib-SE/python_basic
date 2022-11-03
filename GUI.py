from tkinter import Tk
from tkinter import *
root = Tk()
root.option_add("*Font", "aerial")
root.geometry("600x600")
name = StringVar()


def myfuction():
    print("You click me")
    name.set("You click me")
Label(root,text="Form").place(x=200,y=10)    
Label(root, text="Enter Your name").place(x=20, y=50)
Entry(root, width=30, textvariable=name).place(x=160, y=50)
Label(root, text="Enter Your password").place(x=20, y=150)
Entry(root, width=30, textvariable=name).place(x=180, y=150)
Button(root, text="Login", bg="blue", fg="white", height=1,
width=10, command="myfunction").place(x=200, y=300)


# A =Label(root,text="this is arial")
# A.place(x=100,y=30)
# L = Label(root, text="This is my first GUI application")
# L.place(x=100, y=100)
root.mainloop()
