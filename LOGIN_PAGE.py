
from tkinter import *
import mysql.connector
from tkinter import messagebox


root = Tk()
root.title("LOGIN PAGE")

# SETTING THE SIZE
root.geometry("850x400")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')

# USERNAME
user_LBL = Label(root, text="Name ", bg="white", font="calibri 15 bold")
user_LBL.place(x=80, y=80)
user_Ent = Entry(root, font="calibri 14 bold", width=21)
user_Ent.place(x=80, y=120)

# PASSWORD
pass_LBL = Label(root, text="ID Number ", bg="white", font="calibri 15 bold")
pass_LBL.place(x=80, y=180)
pass_Ent = Entry(root, font="calibri 14 bold", width=21)
pass_Ent.place(x=80, y=220)

# SIGN IN


def sign_in():

    connect = mysql.connector.connect(host="localhost", user="lifechoices", password="@Lifechoices1234",
                                      database="lifechoicesonline")
    conn = connect.cursor()
    conn.execute("SELECT * FROM User")
    verify = False
    for i in conn:
        # current = int(i[0]) + 1
        if user_Ent.get() == i[1] and pass_Ent.get() == i[4]:
            verify = True
            sqlstatement= "UPDATE User SET date_time_in = curtime() WHERE No= " + str(i[0])
            conn.execute(sqlstatement)
            connect.commit()
            print(conn.rowcount)
            messagebox.showinfo(message="Successfully logged in")
    if not verify:
        messagebox.showerror(message="User not register")

def sign_out():

    connect = mysql.connector.connect(host="localhost", user="lifechoices", password="@Lifechoices1234",
                                      database="lifechoicesonline")
    conn = connect.cursor()
    conn.execute("SELECT * FROM User")
    verify = False
    for i in conn:
        # current = int(i[0]) + 1
        if user_Ent.get() == i[1] and pass_Ent.get() == i[4]:
            verify = True
            sqlstatement= "UPDATE User SET date_time_out = curtime() WHERE No= " + str(i[0])
            conn.execute(sqlstatement)
            connect.commit()
            print(conn.rowcount)
            messagebox.showinfo(message="Successfully logged out")
    if not verify:
        messagebox.showerror(message="User not register")




user_signin_Btn = Button(root, text="Sign In", borderwidth="1", bg="#187bcd", fg="black", font="calibri 15 bold", width=7,
                        activebackground="white", command=sign_in)
user_signin_Btn.place(x=80, y=280)

user_signout_Btn = Button(root, text="Sign Out", borderwidth="1", bg="#187bcd", fg="black", font="calibri 15 bold", width=7,
                        activebackground="white", command=sign_out)
user_signout_Btn.place(x=230, y=280)
# ADMIN HEADING
admin_LBL = Label(root, text="Admin Sign In Here ", bg="white", font="Times 20 bold underline")
admin_LBL.place(x=500, y=10)

users_LBL = Label(root, text="Users Sign In Here ", bg="white", font="Times 20 bold underline")
users_LBL.place(x=80, y=10)
# ADMIN USERNAME
user2_LBL = Label(root, text="Name ", bg="white", font="calibri 15 bold")
user2_LBL.place(x=500, y=80)
user2_Ent = Entry(root, font="calibri 14 bold", width=21)
user2_Ent.place(x=500, y=120)

# ADMIN PASSWORD
pass2_LBL = Label(root, text="Password", bg="white", font="calibri 15 bold")
pass2_LBL.place(x=500, y=180)
pass2_Ent = Entry(root, font="calibri 14 bold", width=21)
pass2_Ent.place(x=500, y=220)


def admin_rights():
    if user2_Ent.get() != "lifechoices":
        messagebox.showerror(message="Please enter correct Admin details")
    elif pass2_Ent.get() != "lifechoices1234":
        messagebox.showerror(message="Please enter correct Admin password")

    else:
        if user2_Ent.get() == "lifechoices" and pass2_Ent.get() == "lifechoices1234":
            messagebox.showinfo("Access Granted", "Welcome Admin")
            root.destroy()
            import admin_page


        else:
            pass


# LOGIN BUTTON
login_Btn = Button(root, text="Login", borderwidth="1", bg="#187bcd", fg="black", font="calibri 15 bold", width=18, activebackground="white", command=admin_rights)
login_Btn.place(x=500, y=280)

# REGISTER BUTTON
def nextscreen():
    root.destroy()
    import register_page


register_LBL = Label(root, text="Not registered?", bg="white")
register_LBL.place(x=110, y=330)
register_BTN = Button(root, text="Register here", bg="white", fg="red", highlightbackground="white",
                      activebackground="white", border="0", command=nextscreen)
register_BTN.place(x=215, y=325)
root.mainloop()
