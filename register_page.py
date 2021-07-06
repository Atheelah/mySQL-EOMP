from tkinter import *

root = Tk()
root.title("REGISTER PAGE")

# SETTING THE SIZE
root.geometry("450x450")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')

detail_LBL = Label(root, text="Your Details Here", bg="white", font="calibri 15 bold")
detail_LBL.place(x=120, y=5)

# NAME LABEL AND ENTRIES
name_LBL = Label(root, text="Name", font="calibri 12 bold", bg="#187cbd", width=10)
name_LBL.place(x=20, y=50)
name_Ent = Entry(root, font="calibri 10 bold", width=21)
name_Ent.place(x=135, y=50)

# EMAIL LABEL AND ENTRIES
email_LBL = Label(root, text="Email", font="calibri 12 bold", bg="#187cbd", width=10)
email_LBL.place(x=20, y=100)
email_Ent = Entry(root, font="calibri 10 bold", width=21)
email_Ent.place(x=135, y=100)

phone_LBL = Label(root, text="Phone No.", font="calibri 12 bold", bg="#187cbd", width=10)
phone_LBL.place(x=20, y=150)
phone_Ent = Entry(root, font="calibri 10 bold", width=21)
phone_Ent.place(x=135, y=150)

next_detail_LBL = Label(root, text="Next Of Kin Details Here", bg="white", font="calibri 15 bold")
next_detail_LBL.place(x=60, y=200)

name_LBL = Label(root, text="Name", font="calibri 12 bold", bg="#187cbd", width=10)
name_LBL.place(x=20, y=250)
name_Ent = Entry(root, font="calibri 10 bold", width=21)
name_Ent.place(x=135, y=250)

phone_LBL = Label(root, text="Phone No.", font="calibri 12 bold", bg="#187cbd", width=10)
phone_LBL.place(x=20, y=300)
phone_Ent = Entry(root, font="calibri 10 bold", width=21)
phone_Ent.place(x=135, y=300)

register_LBL = Label(root, text="Already registered?", bg="white")
register_LBL.place(x=60, y=350)


def nextscreen():
    root.destroy()
    import LOGIN_PAGE


register_BTN = Button(root, text="Login With Details", bg="white", fg="red", highlightbackground="white",
                      activebackground="white", border="0", command=nextscreen)
register_BTN.place(x=190, y=345)

root.mainloop()
