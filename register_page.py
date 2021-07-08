from tkinter import *
import mysql.connector
root = Tk()
root.title("REGISTER PAGE")

# SETTING THE SIZE
root.geometry("450x600")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')




def insert():
    connect = mysql.connector.connect(host="localhost", user="lifechoices", password="@Lifechoices1234",
                                      database="lifechoicesonline")
    conn = connect.cursor()
    conn.execute("SELECT * FROM User")
    current = 0
    for i in conn:
        current = int(i[0]) + 1
    sqlstatement ="INSERT INTO User(No, Name, Phone, Email, ID) VALUES("+str(current)+",%s, %s, %s, %s)"
    sqlvalue=(name_Ent.get(), phone_Ent.get(), email_Ent.get(), ID_Ent.get())
    conn.execute(sqlstatement, sqlvalue)
    sqlstatement = "INSERT INTO nextofkin(Name, Phone, UserNo) VALUES(%s, %s, %s)"
    sqlvalue = (name2_Ent.get(), phone2_Ent.get(), str(current))
    conn.execute(sqlstatement, sqlvalue)
    conn.execute("SELECT * FROM User")
    current = 0
    for i in conn:
        print(i)
    conn.execute("SELECT * FROM nextofkin")
    current = 0
    for i in conn:
        # current = int(i[0]) + 1
        print(i)
    connect.commit()
    root.destroy()
    import LOGIN_PAGE
# insert()


detail_LBL = Label(root, text="Your Details Here", bg="white", font="calibri 15 bold")
detail_LBL.place(x=120, y=10)

# NAME LABEL AND ENTRIES
name_LBL = Label(root, text="Name", font="calibri 12 bold", bg="#187cbd", width=10)
name_LBL.place(x=60, y=70)
name_Ent = Entry(root, font="calibri 10 bold", width=22)
name_Ent.place(x=175, y=70)

# EMAIL LABEL AND ENTRIES
email_LBL = Label(root, text="Email", font="calibri 12 bold", bg="#187cbd", width=10)
email_LBL.place(x=60, y=120)
email_Ent = Entry(root, font="calibri 10 bold", width=22)
email_Ent.place(x=175, y=120)

phone_LBL = Label(root, text="Phone No.", font="calibri 12 bold", bg="#187cbd", width=10)
phone_LBL.place(x=60, y=170)
phone_Ent = Entry(root, font="calibri 10 bold", width=22)
phone_Ent.place(x=175, y=170)

ID_LBL = Label(root, text="ID Number.", font="calibri 12 bold", bg="#187cbd", width=10)
ID_LBL.place(x=60, y=220)
ID_Ent = Entry(root, font="calibri 10 bold", width=22)
ID_Ent.place(x=175, y=220)

next_detail_LBL = Label(root, text="Next Of Kin Details Here", bg="white", font="calibri 15 bold")
next_detail_LBL.place(x=80, y=310)

name2_LBL = Label(root, text="Name", font="calibri 12 bold", bg="#187cbd", width=10)
name2_LBL.place(x=60, y=360)
name2_Ent = Entry(root, font="calibri 10 bold", width=22)
name2_Ent.place(x=175, y=360)

phone2_LBL = Label(root, text="Phone No.", font="calibri 12 bold", bg="#187cbd", width=10)
phone2_LBL.place(x=60, y=410)
phone2_Ent = Entry(root, font="calibri 10 bold", width=22)
phone2_Ent.place(x=175, y=410)



def nextscreen():
    root.destroy()
    import LOGIN_PAGE


register2_Btn = Button(root, text="Register", borderwidth="1", bg="#187bcd", fg="black", font="calibri 15 bold", width=21,
                      activebackground="white", command=insert)
register2_Btn.place(x=60, y=480)

register_LBL = Label(root, text="Already registered?", bg="white")
register_LBL.place(x=80, y=550)

login_BTN = Button(root, text="Login With Details", bg="white", fg="red", highlightbackground="white",
                      activebackground="white", border="0", command=nextscreen)
login_BTN.place(x=210, y=545)


root.mainloop()
