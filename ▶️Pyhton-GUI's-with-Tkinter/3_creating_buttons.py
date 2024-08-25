from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='Lock! I clicked a Button!!')
    myLabel.pack()

# We can add a state parameter and set it up to DISABLED
myButton = Button(root, text='Click Me!', padx=50, pady= 50, command=myClick, fg='white', bg='black')
myButton.pack()

root.mainloop()