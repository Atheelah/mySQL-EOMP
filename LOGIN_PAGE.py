# LOGIN PAGE

from tkinter import *

root = Tk()
root.title("LOGIN PAGE")

# SETTING THE SIZE
root.geometry("450x300")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')

# USERNAME
user_LBL = Label(root, text="Name ", bg="white", font="calibri 15 bold")
user_LBL.place(x=80, y=5)
user_Ent = Entry(root, font="calibri 14 bold", width=21)
user_Ent.place(x=80, y=40)

# PASSWORD
pass_LBL = Label(root, text="ID Number ", bg="white", font="calibri 15 bold")
pass_LBL.place(x=80, y=80)
pass_Ent = Entry(root, font="calibri 14 bold", width=21)
pass_Ent.place(x=80, y=120)

# LOGIN BUTTON
login_Btn = Button(root, text="Login", borderwidth="1", bg="#187bcd", fg="black", font="calibri 15 bold", width=18, activebackground="white")
login_Btn.place(x=80, y=180)

# REGISTER BUTTON
def nextscreen():
    root.destroy()
    import register_page


register_LBL = Label(root, text="Not registered?", bg="white")
register_LBL.place(x=80, y=250)
register_BTN = Button(root, text="Register here", bg="white", fg="red", highlightbackground="white",
                      activebackground="white", border="0", command=nextscreen)
register_BTN.place(x=185, y=245)
root.mainloop()
