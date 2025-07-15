import tkinter as tk
from tkinter import messagebox, ttk
import threading
import time
import pygame
from datetime import datetime

pygame.mixer.init()

timer_thread = None
is_paused = False
stop_flag = False

def start_timer():
    global timer_thread, is_paused, stop_flag

    try:
        total_seconds = int(hours.get()) * 3600 + int(minutes.get()) * 60 + int(seconds.get())
        if total_seconds <= 0:
            raise ValueError

        log_time_entry(total_seconds)

        is_paused = False
        stop_flag = False
        max_seconds = total_seconds

        def countdown():
            nonlocal total_seconds
            start_button.config(state="disabled")
            pause_button.config(state="normal")
            stop_button.config(state="normal")

            while total_seconds > 0 and not stop_flag:
                if not is_paused:
                    mins, secs = divmod(total_seconds, 60)
                    hrs, mins = divmod(mins, 60)
                    timer_var.set(f"{hrs:02}:{mins:02}:{secs:02}")
                    progress['value'] = (max_seconds - total_seconds) / max_seconds * 100
                    time.sleep(1)
                    total_seconds -= 1
                else:
                    time.sleep(0.1)

            if not stop_flag and not is_paused:
                timer_var.set("00:00:00")
                progress['value'] = 100
                try:
                    pygame.mixer.Sound("alarm.mp3").play()
                except Exception as e:
                    print(f"Error playing sound: {e}")
                messagebox.showinfo("Timer Done", "Time's up!")

            start_button.config(state="normal")
            pause_button.config(state="disabled", text="Pause")
            stop_button.config(state="disabled")

        timer_thread = threading.Thread(target=countdown, daemon=True)
        timer_thread.start()

    except ValueError:
        messagebox.showwarning("Invalid input", "Please enter valid numbers (HH MM SS > 0).")

def pause_resume_timer():
    global is_paused
    is_paused = not is_paused
    pause_button.config(text="Resume" if is_paused else "Pause")

def stop_timer():
    global stop_flag
    stop_flag = True
    timer_var.set("00:00:00")
    progress['value'] = 0
    start_button.config(state="normal")
    pause_button.config(state="disabled", text="Pause")
    stop_button.config(state="disabled")

def log_time_entry(seconds):
    hrs, rem = divmod(seconds, 3600)
    mins, secs = divmod(rem, 60)
    log_entry = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Set Timer: {hrs:02}:{mins:02}:{secs:02}\n"
    with open("timer_logs.txt", "a") as f:
        f.write(log_entry)

root = tk.Tk()
root.title("Enhanced Countdown Timer")
root.geometry("350x300")
root.resizable(False, False)

tk.Label(root, text="Enter Time (HH MM SS):").pack(pady=5)

frame = tk.Frame(root)
frame.pack()

hours = tk.Entry(frame, width=4)
hours.pack(side="left", padx=3)
minutes = tk.Entry(frame, width=4)
minutes.pack(side="left", padx=3)
seconds = tk.Entry(frame, width=4)
seconds.pack(side="left", padx=3)

timer_var = tk.StringVar(value="00:00:00")
tk.Label(root, textvariable=timer_var, font=("Helvetica", 32), fg="blue").pack(pady=10)

progress = ttk.Progressbar(root, length=250, mode='determinate')
progress.pack(pady=5)

start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=5)

pause_button = tk.Button(root, text="Pause", command=pause_resume_timer, state="disabled")
pause_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop/Reset", command=stop_timer, state="disabled")
stop_button.pack(pady=5)

root.mainloop()