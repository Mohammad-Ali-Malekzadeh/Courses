# ====================//import//==================
from tkinter import *
import tkinter.messagebox

# ====================//Settings//==================
root = Tk()
root.title("Calculator")
root.geometry("400x250")
root.resizable(width=False, height=False)
color = "gray"
root.configure(bg=color)
# ====================//Variable//==================
num1 = StringVar()
num2 = StringVar()
res = StringVar()
# ====================//Frames//==================
First_frame = Frame(root, width=400, height=50, bg=color)
First_frame.pack(side="top")
Second_frame = Frame(root, width=400, height=50, bg=color)
Second_frame.pack(side="top")
Third_frame = Frame(root, width=400, height=50, bg=color)
Third_frame.pack(side="top")
Forth_frame = Frame(root, width=400, height=50, bg=color)
Forth_frame.pack(side="top")
Five_frame = Frame(root, width=400, height=50, bg=color)
Five_frame.pack(side="top")
# ====================//Buttons//==================
btn_plus = Button(
    Forth_frame, text="+", width=10, highlightbackground=color, command=lambda: minus()
)
btn_plus.pack(side=LEFT, padx=5, pady=5)
btn_plus = Button(
    Forth_frame, text="-", width=10, highlightbackground=color, command=lambda: plus()
)
btn_plus.pack(side=LEFT, padx=5, pady=5)
btn_plus = Button(
    Forth_frame, text="*", width=10, highlightbackground=color, command=lambda: mul()
)
btn_plus.pack(side=LEFT, padx=5, pady=5)
btn_plus = Button(
    Forth_frame, text="/", width=10, highlightbackground=color, command=lambda: div()
)
btn_plus.pack(side=LEFT, padx=5, pady=5)
btn_plus = Button(
    Five_frame,
    text="Clear",
    width=10,
    highlightbackground=color,
    command=lambda: clear(),
)
btn_plus.pack(side=LEFT, padx=5, pady=5)
btn_plus = Button(
    Five_frame,
    text="Creator",
    width=10,
    highlightbackground=color,
    command=lambda: creator(),
)
btn_plus.pack(side=LEFT, padx=5, pady=5)


# ====================//Functions//==================
def error_Msg(ms):
    if ms == "error":
        tkinter.messagebox.showerror("Error", "Something Went Wrong")
    elif ms == "Division Error":
        tkinter.messagebox.showerror("Division Error", "can not divide by 0")


def plus():
    try:
        value = float(num1.get()) + float(num2.get())
        res.set(value)
    except:
        error_Msg("error")


def minus():
    try:
        value = float(num1.get()) - float(num2.get())
        res.set(value)
    except:
        error_Msg("error")


def mul():
    try:
        value = float(num1.get()) * float(num2.get())
        res.set(value)
    except:
        error_Msg("error")


def div():
    if num2.get() == "0":
        error_Msg("Division Error")
    elif num2.get() != "0":
        try:
            value = float(num1.get()) / float(num2.get())
            res.set(value)
        except:
            error_Msg("error")


def clear():
    num1.set("")
    num2.set("")
    res.set("")


def creator():
    tkinter.messagebox.showinfo(
        "Creator", "calculator has been created by Mohammad Ali Malekzadeh."
    )


# ====================//Label & Entrys//==================
label_first_num = Label(First_frame, text="Enter First Number:", bg=color)
label_first_num.pack(side=LEFT, padx=5, pady=5)
first_num = Entry(First_frame, highlightbackground=color, textvariable=num1)
first_num.pack(side=LEFT)
label_second_num = Label(Second_frame, text="Enter Second Number:", bg=color)
label_second_num.pack(side=LEFT, padx=5, pady=5)
second_num = Entry(Second_frame, highlightbackground=color, textvariable=num2)
second_num.pack(side=LEFT)
num_result = Label(Third_frame, text="Result", bg=color)
num_result.pack(side=LEFT, padx=5, pady=5)
result = Entry(Third_frame, highlightbackground=color, textvariable=res)
result.pack(side=LEFT, padx=5, pady=5)
# ====================//Run//==================
root.mainloop()
