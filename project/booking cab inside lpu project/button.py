from tkinter import *

root = Tk()

button = Button(root, text="Click me!",height=100,width=100)
img = PhotoImage(file="login.gif") # make sure to add "/" not "\"
button.config(image=img)
button.pack() # Displaying the button

root.mainloop()
