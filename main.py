import tkinter as tk
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
RED = "#ff0000"
BLUE = "#37b7c3"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK_MARK = "✓"
TOMATO_IMAGE_PATH = "tomato.png"

round = 1
check_mark_quantity = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global round, check_mark_quantity
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    check_mark_quantity = 0
    check_mark_label.config(text=CHECK_MARK * check_mark_quantity)
    round = 1

def focus_window(option):
    if option == "on":
        window.deiconify()
        window.focus_force()
        window.attributes('-topmost', 1)
    elif option == "off":
        window.attributes('-topmost', 0)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global round, check_mark_quantity
    if round < 9:
        if round % 2 == 1:
            timer_label.config(text="STUDY")
            timer_label.config(fg=GREEN)
            count_time = WORK_MIN * 60
            count_down(count_time)
            focus_window("off")
            window.bell()
        else:
            check_mark_quantity += 1
            check_mark_label.config(text=CHECK_MARK * check_mark_quantity)
            focus_window("on")
            window.bell()
            if round % 8 == 0:
                timer_label.config(text="LONG BREAK")
                timer_label.config(fg=RED)
                count_time = LONG_BREAK_MIN * 60
                count_down(count_time)
            elif round % 2 == 0:
                timer_label.config(text="SHORT BREAK")
                timer_label.config(fg=BLUE)
                count_time = SHORT_BREAK_MIN * 60
                count_down(count_time)
        round += 1
    else:
        reset_timer()
        round = 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_mins = floor(count / 60)
    count_secs = int(count % 60)
    if count_mins < 10:
        count_mins = f"0{count_mins}"
    if count_secs == 0:
        count_secs = "00"
    elif int(count_secs) < 10:
        count_secs = f"0{count_secs}"
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tk.PhotoImage(file=TOMATO_IMAGE_PATH)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = tk.Label(text="TIMER", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = tk.Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark_label = tk.Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark_label.grid(row=3, column=1)

window.mainloop()