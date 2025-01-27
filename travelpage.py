from tkinter import *
root = Tk()
root.geometry("600x400")
root.minsize(600, 400)  #minimum size of gui...it can be enlarged but cannot get smaller than this...same for maxsize
root.title("travel page")

def main():
    print("it works!")

Label(root,text="welcome to bunny travels", font="arial 16 bold").grid(row=0, column=1,pady=10)
password = Label(root,text="password")
password.grid(row=1, column=0)
passvalue = StringVar()
passentry = Entry(root,textvariable=passvalue)
passentry.grid(row=1, column=1)

def passw():
    if (passvalue.get() == "helloworld"):
        name = Label(root,text="name")
        gender = Label(root,text="gender")
        phone = Label(root,text="phone number")
        email = Label(root,text="email")
        foodservice = Label(root,text="food service")

        name.grid(row=3, column=0,pady=10)
        gender.grid(row=4, column=0,pady=10)
        phone.grid(row=5, column=0,pady=10)
        email.grid(row=6, column=0,pady=10)

        namevalue = StringVar()
        gvalue = StringVar()
        pvalue = StringVar()
        evalue = StringVar()
        foodservicevalue = IntVar()

        nentry = Entry(root,textvariable=namevalue)
        genderentry = Entry(root,textvariable=gvalue)
        pentry = Entry(root,textvariable=pvalue)
        eentry = Entry(root,textvariable=evalue)

        nentry.grid(row=3, column=1,pady=10)
        genderentry.grid(row=4, column=1,pady=10)
        pentry.grid(row=5, column=1,pady=10)
        eentry.grid(row=6, column=1,pady=10)

        foodservice = Checkbutton(root,text="prebook your meals?", variable=foodservicevalue)
        foodservice.grid(row=7, column=1,pady=10)

        Button(text="submit",command=main).grid(row=8,column=1,pady=10)

    else:
        print("incorrect password")

Button(root,text="enter",command=passw).grid(row=2, column=1)
root.mainloop()