import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
timer = None
new_list = {}


def new_card(button="None"):
    global new_list, flip_time, learned_dictionary, learned
    if len(learned_dictionary) < 3:

        if button == "tick":
            df = pandas.DataFrame([new_list])
            df.to_csv("words_learned.csv", mode='a', index=False, header=False)
            learned = pandas.read_csv("words_learned.csv")
            learned_dictionary = [{"German": row["German"], "English": row["English"]} for _, row in learned.iterrows()]
            canvas.itemconfig(progress, text=f"Words Learned: {len(learned_dictionary)}/1000")

        window.after_cancel(flip_time)
        new_list = random.choice(words_dictionary)
        if len(learned_dictionary) < 3:
            while new_list in learned_dictionary:
                new_list = random.choice(words_dictionary)
            new_word = new_list["German"]
            canvas.itemconfig(word, text=new_word, fill="black")
            canvas.itemconfig(card, image=front_image)
            canvas.itemconfig(title, text="German", fill="black")

            flip_time = window.after(3000, flip_card)

    else:
        canvas.itemconfig(title, text="You have memorized the \n1000 Basic German Words", fill="black")
        canvas.itemconfig(word, text="Congratulations", fill="black")
        check_button.config(state="disabled")
        cross_button.config(state="disabled")


def flip_card():
    translation = new_list["English"]
    canvas.itemconfig(card, image=back_image)
    canvas.itemconfig(word, fill="white", text = translation)
    canvas.itemconfig(title, text="English", fill="white")


data = pandas.read_csv("german_words.csv")
learned = pandas.read_csv("words_learned.csv")
words_dictionary = [{"German": row["German"], "English": row["English"]} for _, row in data.iterrows()]
learned_dictionary = [{"German": row["German"], "English": row["English"]} for _, row in learned.iterrows()]

window = Tk()
window.title("VocabPoP")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
if len(learned_dictionary) < 3:
    flip_time = window.after(3000,func=flip_card)


canvas = Canvas(height=530, width=820,bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(420, 275, image=front_image)
title = canvas.create_text(420,150, font=("Ariel", 40, "italic"))
word = canvas.create_text(420,300, font=("Ariel", 60, "bold"))
progress = canvas.create_text(690,490,text=f"Words Learned: {len(learned_dictionary)}/1000", font=("Ariel",10,"italic"))
canvas.grid(column=1, row=1, columnspan=2)

# Adding Buttons
check_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_image, highlightthickness=0, relief="flat", bd=0, command=lambda: new_card("tick"))
check_button.grid(column=1, row=2, pady=(40, 10))

cross_image = PhotoImage(file="./images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, relief="flat", bd=0, command=lambda: new_card("cross"))
cross_button.grid(column=2, row=2, pady=(40, 10))
new_card()

window.mainloop()
