from tkinter import *
root = Tk()
root.title("Welcome")

# SETTING THE SIZE
root.geometry("350x300")

# THE USER CANT MAXIMIZE THE WINDOW
root.resizable(height=False, width=False)

# SETTING THE BACKGROUND COLOR
root.config(bg='white')

# SHOWING THE MESSAGE
message_LBL = Label(root, text="Welcome To ", bg="white", font=("Consolas 25 bold"))
message_LBL.place(x=60, y=10)
# ADDING AN IMAGE
photo = PhotoImage(file="Screenshot from 2021-07-05 14-24-43.png")
label = Label(root, image=photo)
label.place(x=30, y=70)


def nextscreen():
    root.destroy()
    import LOGIN_PAGE


next_BTN = Button(root, text="Next",  font=("Consolas 15 bold"), width="10", borderwidth="4", bg="green", command=nextscreen)
next_BTN.place(x=100, y=200)



# ALLOWING THE SCREEN TO RUN
root.mainloop()

