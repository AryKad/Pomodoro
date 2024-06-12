from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #


def restart_timer():
    window.after_cancel(TIMER)
    my_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timertext, text="00:00")
    tick_label.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    print(REPS)
    if REPS % 8 == 0:
        countdown(int(LONG_BREAK_MIN * 60))
        my_label.config(text="BREAK", fg=RED)
        tick_label.config(text="✔️" * int(REPS / 2))
    elif REPS % 2 == 0:
        countdown(int(SHORT_BREAK_MIN * 60))
        my_label.config(text="BREAK", fg=PINK)
        tick_label.config(text="✔️" * int(REPS / 2))
    else:
        countdown(int(WORK_MIN * 60))
        my_label.config(text="WORK")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timertext, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
pic = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=pic)
timertext = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 18, "bold"))
canvas.grid(row=1, column=1)

my_label = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
my_label.grid(row=0, column=1)
tick_label = Label(font="bold", fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)

start_button = Button(text="Start", font=FONT_NAME, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", font=FONT_NAME, command=restart_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
