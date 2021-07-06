from tkinter import *

root = Tk()
root.title("LOGIN PAGE")

# SETTING THE SIZE
root.geometry("450x300")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')

detail_LBL = Label(root, text="Your Details Here", bg="white", font="calibri 15 bold")
detail_LBL.place(x=120, y=5)

name_LBL = Label(root, text="Password ", bg="#187cbd", font="calibri 15 bold")
name_LBL.place(x=20, y=50)
name_Ent = Entry(root, font="calibri 14 bold", width=21)
name_Ent.place(x=135, y=50)

root.mainloop()
