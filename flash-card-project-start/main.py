import tkinter as tk
from tkinter import Button, PhotoImage
import pandas as pd
import random


data=pd.read_csv("data/french_words.csv")
def recall():
    return  random.randint(0, len(data) - 1)

def right():
    global j
    j=recall()
    infor=data.English[j]
    canvas.itemconfig(card_back_image, image=card_back)
    title_label.config(text=infor,bg="#B1DDC6")
def wrong():
    global j
    info=data.French[j]
    canvas.itemconfig(card_back_image, image=card_front)
    title_label.config(text=info,bg="white")




BACKGROUND_COLOR = "#B1DDC6"
window = tk.Tk()
window.title("Flash Card")

canvas = tk.Canvas(window, width=800, height=526)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front = PhotoImage(file="./images/card_front.png")
card_back=tk.PhotoImage(file="./images/card_back.png")
card_back_image=canvas.create_image(400, 263, image=card_back)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=1,columnspan=2)
wrong_image=tk.PhotoImage(file="./images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=wrong)
wrong_button.grid(row=2,column=2,padx=10,pady=10)
right_image=tk.PhotoImage(file="./images/right.png")
right_button=Button(image=right_image,highlightthickness=0,bg=BACKGROUND_COLOR,command=right)
right_button.grid(row=2,column=1,padx=10,pady=10)
title_label=tk.Label(text="Flash Card",fg="black",font=("Arial",30))
title_label.grid(row=1,column=1,columnspan=2)
window.mainloop()
