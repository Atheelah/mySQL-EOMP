import mysql.connector
from tkinter import *
from tkinter import ttk


root = Tk()
root.title("LOGIN PAGE")

# SETTING THE SIZE
root.geometry("450x500")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')

connect = mysql.connector.connect(host="localhost", user="lifechoices", password="@Lifechoices1234", database="lifechoicesonline")
conn = connect.cursor()
conn.execute("SELECT * FROM User")
tree = ttk.Treeview(root)

tree["columns"] = ("No", "Name", "Email", "Phone", "ID", "date_time")

tree.column("No", width=50, minwidth=50, anchor=CENTER)
tree.column("Name", width=50, minwidth=50, anchor=CENTER)
tree.column("Email", width=50, minwidth=50, anchor=CENTER)
tree.column("Phone", width=50, minwidth=50, anchor=CENTER)
tree.column("ID", width=50, minwidth=50, anchor=CENTER)
tree.column("date_time", width=50, minwidth=50, anchor=CENTER)

tree.heading("No", text="No", anchor=CENTER)
tree.heading("Name", text="Name", anchor=CENTER)
tree.heading("Email", text="Email", anchor=CENTER)
tree.heading("Phone", text="Phone", anchor=CENTER)
tree.heading("ID", text="ID", anchor=CENTER)
tree.heading("date_time", text="date_time", anchor=CENTER)

i = 0
for ro in conn:
    tree.insert('', i, text="", values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5]))
    i = i + 1
# tree.pack()













# USERNAME
user_LBL = Label(root, text="Name ", bg="white", font="calibri 15 bold")
user_LBL.place(x=80, y=10)
user_Ent = Entry(root, font="calibri 14 bold", width=21)
user_Ent.place(x=80, y=40)

# PASSWORD
pass_LBL = Label(root, text="ID Number ", bg="white", font="calibri 15 bold")
pass_LBL.place(x=80, y=80)
pass_Ent = Entry(root, font="calibri 14 bold", width=21)
pass_Ent.place(x=80, y=120)

# ADMIN HEADING
admin_LBL = Label(root, text="Admin Sign In Here ", bg="white", font="Times 20 bold underline")
admin_LBL.place(x=100, y=180)

# ADMIN USERNAME
user_LBL = Label(root, text="Name ", bg="white", font="calibri 15 bold")
user_LBL.place(x=80, y=5)
user_Ent = Entry(root, font="calibri 14 bold", width=21)
user_Ent.place(x=80, y=260)

# ADMIN PASSWORD
pass_LBL = Label(root, text="Password", bg="white", font="calibri 15 bold")
pass_LBL.place(x=80, y=330)
pass_Ent = Entry(root, font="calibri 14 bold", width=21)
pass_Ent.place(x=80, y=370)


# LOGIN BUTTON
login_Btn = Button(root, text="Login", borderwidth="1", bg="#187bcd", fg="black", font="calibri 15 bold", width=18, activebackground="white")
login_Btn.place(x=80, y=410)

# REGISTER BUTTON
def nextscreen():
    root.destroy()
    import register_page


register_LBL = Label(root, text="Not registered?", bg="white")
register_LBL.place(x=110, y=460)
register_BTN = Button(root, text="Register here", bg="white", fg="red", highlightbackground="white",
                      activebackground="white", border="0", command=nextscreen)
register_BTN.place(x=215, y=455)
root.mainloop()
