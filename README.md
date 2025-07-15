# Countdown-Timer-With-Alarm-Sound

# ⏳ Countdown Timer (Tkinter + Python)

A feature-rich **countdown timer GUI application** built using Python's `tkinter`, with additional functionality such as audio alarms, logging, pause/resume, and a visual progress bar. Optimized for use with **Pydroid 3** on Android.

---

## 🚀 Features

- ⏱️ Set custom countdown time (Hours, Minutes, Seconds)
- ▶️ Start, ⏸ Pause/Resume, ⏹ Stop/Reset timer
- 🔊 Plays alarm sound (`alarm.mp3`) on completion using `pygame`
- 📊 Visual **progress bar** updates live
- 📝 Logs each timer session to `timer_logs.txt`
- 💡 Clean and responsive Tkinter GUI
- ✅ Fully compatible with **Pydroid 3**

---

## 📸 Screenshots

> _Attach screenshot of the UI or use generated logo/image_

---

## 🔧 Requirements

Make sure to install the following libraries (especially for Pydroid 3 users):

```bash
pip install pygame

> No installation required for tkinter and ttk in standard Python distributions or Pydroid 3.

---

📁 File Structure

📁 countdown-timer/
├── countdown_timer.py       # Main application file
├── alarm.mp3                # Alarm sound (you must provide)
├── timer_logs.txt           # Auto-created log file
└── README.md                # Project description

🎵 Alarm Sound

Place a small alarm.mp3 sound file in the same directory. You can download royalty-free sounds from freesound.org or create a short beep sound using any audio tool.

💻 How to Run

Run the Python script using any Python environment (desktop or Pydroid 3 mobile):

python countdown_timer.py

> For Pydroid 3, simply open the .py file and press "Run".


📌 Future Enhancements

🌓 Dark mode toggle

🔵 Circular progress animation

📲 Notifications or vibration for mobile

🗃 History viewer from logs
