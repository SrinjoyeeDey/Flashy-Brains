BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

current_card={}
to_learn={}

try:
    data=pandas.read_csv("./data/words_toLearn.csv")
except FileNotFoundError:
       
       original_data=pandas.read_csv("./data/French_words.csv")
       to_learn=original_data.to_dict(orient="records")
else:
    to_learn=data.to_dict(orient="records")

def next_card():
        global current_card,flip_timer
        window.after_cancel(flip_timer)
        current_card=random.choice(to_learn)
        canvas.itemconfig(card_title,text="French",fill="black")
        canvas.itemconfig(card_word,text=current_card["French"],fill="black")
        canvas.itemconfig(card_background,image=front_img)
        flip_timer=window.after(3000,func=flip_card)

def flip_card():
        
        canvas.itemconfig(card_title,text="English",fill="white")
        canvas.itemconfig(card_word,text=current_card["English"],fill="white")
        canvas.itemconfig(card_background,image=back_img)

def is_known():
        to_learn.remove(current_card)
        data=pandas.DataFrame(to_learn)
        data.to_csv("./data/words_toLearn.csv", index=False)
        next_card()

window=Tk()

window.title("My Flash Card")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,func=flip_card)


canvas=Canvas(width=800,height=526)

front_img=PhotoImage(file="./images/card_front.png")
back_img=PhotoImage(file="./images/card_back.png")

card_background=canvas.create_image(400,263,image=front_img)

card_title=canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"))
card_word=canvas.create_text(400,263,tex="Word",font=("Ariel",60,"bold"))

cross_img=PhotoImage(file="./images/wrong.png")
unknown_img=Button(image=cross_img,highlightthickness=0,command=flip_card)

right_img=PhotoImage(file="./images/right.png")
correct_img=Button(image=right_img,highlightthickness=0,command=is_known)

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

unknown_img.grid(row=1,column=0)
correct_img.grid(column=1,row=1)

canvas.grid(column=0,row=0,columnspan=2)

next_card()

window.mainloop()