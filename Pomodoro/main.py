import math
from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 * 60
SHORT_BREAK_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60
reps = 0
timer = None
start = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")

    global reps
    reps = 0

    global start
    start = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global start

    if start:
        return
    else:
        start = True

    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN)
        title_label.config(text="Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN)
        title_label.config(text="Break")
    else:
        count_down(WORK_MIN)
        title_label.config(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global start
        start = False
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"

        check_marks.config(text=mark)

        if len(mark) == 4:
            reset_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=GREEN)

title_label = Label(text="Timer", fg=PINK, bg=GREEN, font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

rest_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
rest_button.grid(column=2, row=2)

check_marks = Label(text="", fg=RED, bg=GREEN, font=(FONT_NAME, 15, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()
