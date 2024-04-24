import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pygame
import threading

class AlarmClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Smart Alarm Clock")
        self.geometry("600x400")
        self.current_alarm_time = None
        self.is_alarm_running = False
        self.alarm_sound = pygame.mixer.Sound("file_example_WAV_1MG.wav")

        self.label_time = ttk.Label(self, text="", font=("Helvetica", 48))
        self.label_time.pack(pady=20)

        self.entry_alarm = ttk.Entry(self, font=("Helvetica", 24))
        self.entry_alarm.pack(pady=10)

        self.button_set_alarm = ttk.Button(self, text="Set Alarm", command=self.set_alarm)
        self.button_set_alarm.pack(pady=5)

        self.button_stop_alarm = ttk.Button(self, text="Stop Alarm", command=self.stop_alarm, state="disabled")
        self.button_stop_alarm.pack(pady=5)

        self.update_time()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.label_time.config(text=current_time)

        if self.is_alarm_running:
            self.check_alarm()

        self.after(1000, self.update_time)

    def set_alarm(self):
        alarm_time_str = self.entry_alarm.get()
        try:
            self.current_alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S")
            self.button_set_alarm.config(state="disabled")
            self.button_stop_alarm.config(state="normal")
            self.is_alarm_running = True
        except ValueError:
            self.entry_alarm.delete(0, tk.END)
            self.entry_alarm.insert(0, "Invalid time format")

    def check_alarm(self):
        current_time = datetime.now().time()
        if current_time >= self.current_alarm_time.time():
            self.play_alarm()
        elif self.is_alarm_running:
            self.after(1000, self.check_alarm)

    def play_alarm(self):
        self.is_alarm_running = False
        self.button_set_alarm.config(state="normal")
        self.button_stop_alarm.config(state="disabled")
        self.alarm_sound.play()

    def stop_alarm(self):
        self.is_alarm_running = False
        self.button_set_alarm.config(state="normal")
        self.button_stop_alarm.config(state="disabled")
        self.alarm_sound.stop()

if __name__ == "__main__":
    pygame.mixer.init()
    app = AlarmClock()
    app.mainloop()
