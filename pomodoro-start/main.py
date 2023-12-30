import tkinter as tk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
counting = False
checks = []
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer

    if not (timer is None):
        window.after_cancel(timer)
        state.config(text="Timer", fg=GREEN)
        canvas.itemconfig(timer_text, text="0:00")
        for check in checks:
            check.destroy()
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global counting

    if reps % 2 == 0:
        duration = WORK_MIN
        state.config(text="Work", fg=GREEN)
    elif reps == 7:
        duration = 20
        state.config(text="Break", fg=RED)
    else:
        duration = 5
        state.config(text="Break", fg=PINK)

    count_down(duration)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count, started=False):
    global reps
    # if not started:
    #     count *= 60

    # minutes = count // 60
    minutes = 0
    seconds = count % 60
    text_out = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=text_out)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1, True)
    else:
        if reps % 2 == 0:
            make_check()
        reps += 1
        start_timer()

# ---------------------------- Make checkmarks ------------------------------- #
def make_check():
    # Checkmark creation
    checks.append(tk.Canvas(check_frame, width=35, height=36, bg=YELLOW, highlightthickness=0))
    check = tk.PhotoImage(file="check.png")
    i = len(checks) - 1
    checks[i].create_image(17.5, 18, image=check)
    checks[i].image = check
    checks[i].pack(side="right")
# ---------------------------- UI SETUP ------------------------------- #
# Window configuration

window = tk.Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)




# Tomato photoImage
tomato = tk.PhotoImage(file="tomato.png")

# Canvas creation
canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Button creation
start = tk.Button(window, text="Start", height=1, width=5, command=start_timer)
reset = tk.Button(window, text="Reset", height=1, width=5, command=reset_timer)

# State label
state = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))

# Checkmark frame creation
check_frame = tk.Frame()
check_frame.config(bg=YELLOW)

# Create the grid for things to sit on
state.grid(column=1, row=0)
start.grid(column=0, row=1, pady=(199, 0), padx=(0, 15))
canvas.grid(column=1, row=1)
reset.grid(column=2, row=1, pady=(199, 0), padx=(15, 0))
check_frame.grid(column=1, row=2, pady=(10, 0))


window.mainloop()


