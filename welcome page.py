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
message_LBL = Label(root, text="Welcome To ", bg="white", font=("calibri 25 bold"))
message_LBL.place(x=100, y=10)
# ADDING AN IMAGE
photo = PhotoImage(file="lifechoices.png")
label = Label(root, image=photo)
label.place(x=50, y=70)


def nextscreen():
    root.destroy()
    import LOGIN_PAGE


next_BTN = Button(root, text="Next",  font=("calibri 15 bold"), width="10", bg="#187bcd", command=nextscreen)
next_BTN.place(x=150, y=200)



# ALLOWING THE SCREEN TO RUN
root.mainloop()

