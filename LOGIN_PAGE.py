# LOGIN PAGE

from tkinter import *
root = Tk()
root.title("LOGIN PAGE")

# SETTING THE SIZE
root.geometry("350x350")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
# root.config(bg='grey')

# LABELS
user_LBL = Label(root, text="Please Enter Username : ")
user_LBL.place(x=5, y=5)
user_Ent = Entry(root)
user_Ent.place(x=170, y=5)

# ENTRIES
pass_LBL = Label(root, text="Please Enter Password : ")
pass_LBL.place(x=5, y=50)
pass_Ent = Entry(root)
pass_Ent.place(x=170, y=50)

login_Btn = Button(root, text="Login", borderwidth="3")
login_Btn.place(x=20, y=100)

register = Button(root, text="Register New User", borderwidth="3")
register.place(x=130, y=100)
root.mainloop()
