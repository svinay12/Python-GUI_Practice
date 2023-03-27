from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()

root.title("Calculator Page")
root.geometry("400x400")
root.config(bg="SteelBlue3"  )

def add():
    res= int(val1_entry.get())+int(val2_entry.get())
    print("Addition = ",res)
def sub():
    res= int(val1_entry.get())-int(val2_entry.get())
    print("Subtraction = ",res)
def mul():
    res= int(val1_entry.get())*int(val2_entry.get())
    print("Multiplication = ",res)
def div():
    res= int(val1_entry.get())/int(val2_entry.get())
    print("Division = ",res)

ttk.Label(root,text=" Python - Calculator ",foreground="white",background="SteelBlue3",font=("vardana",18)).pack(pady=(40,30))

lbl1 = ttk.Label(root,text=" FIrst vsalue ",width=20,background="SteelBlue3")
lbl1.pack()
val1_entry = ttk.Entry(root)
val1_entry.pack(padx=5, pady=5)
ttk.Label(root,text=" Second value ",width=20,background="SteelBlue3").pack()
val2_entry = ttk.Entry(root)
val2_entry.pack( padx=5, pady=5)

ttk.Button(root, text="+",command =add).pack(padx=5, pady=5)
ttk.Button(root, text="-",command =sub).pack(padx=5, pady=5)
ttk.Button(root, text="*",command =mul).pack(padx=5, pady=5)
ttk.Button(root, text="/",command =div).pack(padx=5, pady=5)
root.iconbitmap("iconp.ico")


root.mainloop()

