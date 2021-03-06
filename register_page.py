# THIS IS MY REGISTRATION PAGE
# STARTING UP TKINTER AND IMPORTING THE NECESSARY MODULES NEEDED FOR THIS PAGE
from tkinter import *
import mysql.connector
from playsound import playsound
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# SETTING THE TITLE
root = Tk()
root.title("REGISTRATION")

# SETTING THE SIZE
root.geometry("450x600")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')


# DEFINING AN INSERT FUNCTION.
# WHEN THE DATA IS INSERTED INTO THE ENTRIES, PYTHON WILL SEND IT THROUGH mySQL TO PUT IT INTO THE DATABASE
# INTO THE RESPECTED COLUMNS, THEREFORE CREATING A NEW USER.
# THE INFORMATION WILL BE INSERTED INTO THE USER TABLE AND THE NEXT OF KIN TABLE.
# IT IS INDICATED TO PUT IT INTO THE CORRECT TABLE.
# TO THIS I HAVE ADDED AND EMAIL FUNCTION.
# WHEN THE USER PUT IN THEIR EMAIL DETAILS AND AFTER THEY HAVE CLICKED THE REGISTER BUTTON
# AN EMAIL WILL BE SENT TO NOTIFY THEM THAT THEY HAVE REGISTERED.
# WITH THIS EMAIL I HAVE INSERTED A "DING" PLAY SOUND EFFECT

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
        print(i)
    connect.commit()

# PLAY SOUND
    playsound("Ding Sound Effect.mp3")

# BEGINNING OF THE EMAIL
    sender_email_id = "atheelahvanderschyff17@gmail.com"
    receiver_email_id = "{}\n".format(email_Ent.get())
    password = "Av1707004"
    subject = "Life Choices Registration"
    msg = MIMEMultipart()
    msg['From'] = sender_email_id
    msg['To'] = receiver_email_id
    msg['Subject'] = subject
    body = "Good Day, {}\n".format(name_Ent.get())
    body += "\n"
    body += "We hope this email finds you well. \n"
    body += "\n"
    body = body + "You have successfully registered as a user on Life Choices Online.\n"
    body += "\n"
    body = body + "Regards\n"
    body = body + "Life Choices\n"
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(sender_email_id, password)

    # sending the mail
    s.sendmail(sender_email_id, receiver_email_id, text)

    # terminating the session
    s.quit()

# HERE THE LOGIN PAGE IS IMPORTED
    root.destroy()
    import login_page


# DETAILS LABEL
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

# PHONE LABEL AND ENTRIES
phone_LBL = Label(root, text="Phone No.", font="calibri 12 bold", bg="#187cbd", width=10)
phone_LBL.place(x=60, y=170)
phone_Ent = Entry(root, font="calibri 10 bold", width=22)
phone_Ent.place(x=175, y=170)

# ID LABEL AND ENTRIES
ID_LBL = Label(root, text="ID Number.", font="calibri 12 bold", bg="#187cbd", width=10)
ID_LBL.place(x=60, y=220)
ID_Ent = Entry(root, font="calibri 10 bold", width=22)
ID_Ent.place(x=175, y=220)

# NEXT OF KIN LABEL
next_detail_LBL = Label(root, text="Next Of Kin Details Here", bg="white", font="calibri 15 bold")
next_detail_LBL.place(x=80, y=310)

# NAME LABEL AND ENTRIES
name2_LBL = Label(root, text="Name", font="calibri 12 bold", bg="#187cbd", width=10)
name2_LBL.place(x=60, y=360)
name2_Ent = Entry(root, font="calibri 10 bold", width=22)
name2_Ent.place(x=175, y=360)

# PHONE LABEL AND ENTRIES
phone2_LBL = Label(root, text="Phone No.", font="calibri 12 bold", bg="#187cbd", width=10)
phone2_LBL.place(x=60, y=410)
phone2_Ent = Entry(root, font="calibri 10 bold", width=22)
phone2_Ent.place(x=175, y=410)


# DEFINING A FUNCTION TO DESTROY THIS SCREEN AND IMPORT THE LOGIN PAGE
def nextscreen():
    root.destroy()
    import login_page


# CREATED A REGISTER BUTTON
# COMMANDS ARE ADDED WHICH ARE THE FUNCTIONS CREATED ABOVE.
register2_Btn = Button(root, text="Register", borderwidth="1", bg="#187bcd", fg="black", font="calibri 15 bold",
                       width=21, activebackground="white", command=insert)
register2_Btn.place(x=60, y=480)

# REGISTER LABEL
register_LBL = Label(root, text="Already registered?", bg="white")
register_LBL.place(x=80, y=550)

# CREATED A LOGIN BUTTON
# COMMANDS ARE ADDED WHICH ARE THE FUNCTIONS CREATED ABOVE.
login_BTN = Button(root, text="Login With Details", bg="white", fg="red", highlightbackground="white",
                   activebackground="white", border="0", command=nextscreen)
login_BTN.place(x=210, y=545)

# ALLOWING THE GUI TO RUN
root.mainloop()
