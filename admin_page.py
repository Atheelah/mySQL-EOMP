from tkinter import *
import mysql.connector
from tkinter import ttk
root = Tk()
root.title("Database Displayed")

# SETTING THE SIZE
root.geometry("1100x700")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')

s = ttk.Style(root)
s.theme_use("clam")
s.configure("Treeview.Heading", background="#187cbd", foreground="black",  font=("Helvetica", 11, "bold"))

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

nextHeading_LBL = Label(root, text="Table Of Next Of Kin Details ", bg="white", font="Times 20 bold")
nextHeading_LBL.place(x=380, y=340)
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
tree.place(x=250, y=400)

root.mainloop()