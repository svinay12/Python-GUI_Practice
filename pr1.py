from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()

root.title("Login Page")
root.geometry("300x300")
root.config(bg="SteelBlue3"  )

def display_text():
    global username_entry,pass_entry
    str1,str2 = username_entry.get(),pass_entry.get()
    messagebox.showinfo("login","Username : "+str1+"\n Password : "+str2)
    print(str1+"\n"+str2)

ttk.Label(root,text="User Login ",foreground="white",background="SteelBlue3",font=("vardana",18)).pack(pady=(40,30))

lbl1 = ttk.Label(root,text=" Name ",width=20,background="SteelBlue3")
lbl1.pack()
username_entry = ttk.Entry(root)
username_entry.pack(padx=5, pady=5)
ttk.Label(root,text=" Password ",width=20,background="SteelBlue3").pack()
pass_entry = ttk.Entry(root)
pass_entry.pack( padx=5, pady=5)

ttk.Button(root, text="Login",command =display_text).pack(padx=5, pady=5)
root.iconbitmap("iconp.ico")


root.mainloop()

