from tkinter import *
root = Tk()
root.title("Welcome")

# SETTING THE SIZE
root.geometry("450x300")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')

# SHOWING THE MESSAGE
message_LBL = Label(root, text="Welcome To ", bg="white", font=("Times 30 bold"))
message_LBL.place(x=120, y=25)
# ADDING AN IMAGE
photo = PhotoImage(file="lifechoices.png")
label = Label(root, image=photo)
label.place(x=50, y=75)

message_LBL = Label(root, text="Let's  Get  You  Signed  In", font=("Times 15 bold"), bg="white")
message_LBL.place(x=120, y=185)



def nextscreen():
    root.destroy()
    import LOGIN_PAGE


next_BTN = Button(root, text="Next",  font=("calibri 15 bold"), width=24, bg="#187bcd", command=nextscreen, activebackground="white")
next_BTN.place(x=55, y=230)



# ALLOWING THE SCREEN TO RUN
root.mainloop()

