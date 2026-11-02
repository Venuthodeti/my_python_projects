from random import shuffle
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():

    keys=["a","b","c","d","e","f","g","h","i","j","k","l","m","n",'o','p','q','r','s','t','u','v','w','x','y','z']
    numbers=["1","2","3","4","5","6","7","8","9"]
    some=["!","@","#","$","%","&","*"]
    password_0 = [random.choice(keys) for _ in range(5) ]
    password_1=[random.choice(numbers) for _ in range(3) ]
    password_2=[random.choice(some) for _ in range(3) ]
    added_password=password_0+password_1+password_2
    random.shuffle(added_password)
    password="".join(added_password)
    password_entry.delete(0,END)
    password_entry.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def saving():
    website=website_entry.get()
    password=password_entry.get()
    email=email_entry.get()
    if len(website)==0 or len(password)==0 or len(email)==0 or len(website)==0 or len(password)<=0:
        messagebox.showinfo(title="ERROR",message="fill all the details")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"IS IT OK TO SAVE \nYour password is: {password}\nYour email is: {email}\nYour website is: {website}")

        if is_ok:
            with open('data.txt','a') as file:
                file.write(f"{website} | {password} | {email} \n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_entry.delete(0, END)
                email_entry.insert(0, "email")


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window=Tk()
window.title("Password Manager")
canvas=Canvas(window,width=200,height=200,bg="white",highlightthickness=0)
window.config(padx=50,pady=50,bg="white")
image=PhotoImage(file="logo.png")

canvas.create_image(100,100,image=image)
canvas.grid(row=0,column=1)

website_label=Label(text="Website",highlightthickness=0,bg="white")
website_label.grid(row=1,column=0)
password_label=Label(text="Password",highlightthickness=0,bg="white")
password_label.grid(row=2,column=0)
email_label=Label(text="Email",highlightthickness=0,bg="white")
email_label.grid(row=3,column=0)
generate_button=Button(text="Generate",command=generate_password,highlightthickness=0,bg="white")
generate_button.grid(row=2,column=2)
add_button=Button(text="Add",command=saving)
add_button.grid(row=4,column=1,columnspan=2)


website_entry=Entry(width=35,highlightthickness=0,bg="white")
website_entry.grid(row=1,column=1,columnspan=2)
password_entry=Entry(width=20,highlightthickness=0,bg="white")
password_entry.grid(row=2,column=1)
email_entry=Entry(width=35)
email_entry.insert(0,"<EMAIL>")
email_entry.grid(row=3,column=1,columnspan=2)






window.mainloop()


