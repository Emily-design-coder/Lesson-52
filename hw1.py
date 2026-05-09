from tkinter import *
import random

c = ["Rock", "Paper", "Scissors"]

def play(u):
    p = random.choice(c)
    r = "Tie!" if u == p else \
        "Win!" if (u, p) in [("Rock","Scissors"),("Paper","Rock"),("Scissors","Paper")] \
        else "Lose!"
    l.config(text=f"You: {u}\nCPU: {p}\n{r}")

r = Tk()

for i in c:
    Button(r, text=i, command=lambda i=i: play(i)).pack()

Button(r, text="Reset", command=lambda: l.config(text="Play!")).pack()

l = Label(r, text="Play!")
l.pack()

r.mainloop()