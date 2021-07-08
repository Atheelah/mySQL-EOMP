import tkinter
from tkinter import *
import mysql.connector
from tkinter import ttk
root = Tk()
root.title("Database Displayed")

# SETTING THE SIZE
root.geometry("1100x900")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')

s = ttk.Style(root)
s.theme_use("clam")
s.configure("Treeview.Heading",  background="#187cbd", foreground="black",  font=("Helvetica", 11, "bold"))

connect = mysql.connector.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline")
conn = connect.cursor()
conn.execute("SELECT * FROM User")
tree = ttk.Treeview(root)

heading_LBL = Label(root, text="Table Of User Details ", bg="white", font="Times 20 bold")
heading_LBL.place(x=400, y=10)
tree["show"] = "headings"
tree["columns"] = ("No", "Name", "Email", "Phone", "ID", "date_time_in", "date_time_out")

tree.column("No", width=100, minwidth=100, anchor=CENTER)
tree.column("Name", width=200, minwidth=200, anchor=CENTER)
tree.column("Email", width=150, minwidth=150, anchor=CENTER)
tree.column("Phone", width=150, minwidth=150, anchor=CENTER)
tree.column("ID", width=150, minwidth=150, anchor=CENTER)
tree.column("date_time_in", width=150, minwidth=150, anchor=CENTER)
tree.column("date_time_out", width=150, minwidth=150, anchor=CENTER)


tree.heading("No", text="No", anchor=CENTER)
tree.heading("Name", text="Name", anchor=CENTER)
tree.heading("Email", text="Email", anchor=CENTER)
tree.heading("Phone", text="Phone", anchor=CENTER)
tree.heading("ID", text="ID", anchor=CENTER)
tree.heading("date_time_in", text="date_time_in", anchor=CENTER)
tree.heading("date_time_out", text="date_time_out", anchor=CENTER)

i = 0
for ro in conn:
    tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6]))
    i = i + 1
tree.place(x=20, y=80)

connect = mysql.connector.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline")
conn = connect.cursor()
conn.execute("SELECT * FROM nextofkin")
tree = ttk.Treeview(root)


# INSERT BUTTON AND FUNCTION
# HERE A FUNCTION WILL BE CREATED SO THE DATA CAN BE ADDED/INSERTED INTO THE DATABASE
name = tkinter.StringVar()
email = tkinter.StringVar()
phone = tkinter.IntVar()
id = tkinter.StringVar()

def add_data(tree):
    f = Frame(root, width=400, height=320, bg="light blue")
    f.place(x=100, y=250)
    l1 = Label(f, text="Name", width=11, font=("Times 15 bold"), bg="#187cbd")
    l1.place(x=50, y=30)
    e1 = Entry(f, textvariable=name, width=25)
    e1.place(x=170, y=30)

    l2 = Label(f, text="Email", width=10, font=("Times 15 bold"), bg="#187cbd")
    l2.place(x=50, y=70)
    e2 = Entry(f, textvariable=email, width=25)
    e2.place(x=170, y=70)

    l3 = Label(f, text="Phone", width=10, font=("Times 15 bold"), bg="#187cbd")
    l3.place(x=50, y=110)
    e3 = Entry(f, textvariable=phone, width=25)
    e3.place(x=170, y=110)

    l4 = Label(f, text="ID", width=10, font=("Times 15 bold"), bg="#187cbd")
    l4.place(x=50, y=150)
    e4 = Entry(f, textvariable=id, width=25)
    e4.place(x=170, y=150)

    def insert_data():
        nonlocal e1, e2, e3, e4
        s_name = name.get()
        em = email.get()
        ph = phone.get()
        iden = id.get()
        conn.execute("INSERT INTO User(Name, Email, Phone, ID) VALUES(%s, %s, %s, %s)", (s_name, em, ph, iden))
        print(conn.lastrowid)

    submit = Button(f, text="Submit", commmand=None, bg="#187bcd", fg="black", font="Times 15 bold", command=insert_data)
    submit.place(x=100, y=280)
    cancel = Button(f, text="Cancel", commmand=None, bg="#187bcd", fg="black", font="Times 15 bold", command=f.destroy)
    cancel.place(x=200, y=280)

insert_Btn = Button(root, text="Insert", borderwidth="1", bg="#187bcd", fg="black", font="calibri 15 bold", width=15,
                        activebackground="green", comman=lambda:add_data(tree))
insert_Btn.place(x=240, y=350)




delete_Btn = Button(root, text="Sign Out", borderwidth="1", bg="#187bcd", fg="black", font="calibri 15 bold", width=15,
                        activebackground="green", command=None)
delete_Btn.place(x=580, y=350)

nextHeading_LBL = Label(root, text="Table Of Next Of Kin Details ", bg="white", font="Times 20 bold")
nextHeading_LBL.place(x=380, y=440)
tree["show"] = "headings"
tree["columns"] = ("No", "Name", "Phone", "UserNo")
tree.column("No", width=100, minwidth=100, anchor=CENTER)
tree.column("Name", width=200, minwidth=200, anchor=CENTER)
tree.column("Phone", width=200, minwidth=200, anchor=CENTER)
tree.column("UserNo", width=150, minwidth=150, anchor=CENTER)

tree.heading("No", text="No", anchor=CENTER)
tree.heading("Name", text="Name", anchor=CENTER)
tree.heading("Phone", text="Phone", anchor=CENTER)
tree.heading("UserNo", text="UserNo", anchor=CENTER)


i = 0
for ro in conn:
    tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3]))
    i = i + 1
tree.place(x=250, y=500)

root.mainloop()