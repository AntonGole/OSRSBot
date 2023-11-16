import os
from random import *
import time
from pyautogui import sleep


# Method for using the terminal of the OS and inputting commands
def cmd(command):
    os.system(command)


# Use the sleep method from pyautogui with random interval between t1 and t2 both given in milliseconds
def sleep_random(t1, t2):
    sleep(randint(t1, t2)/1000)


# Click random spot inside a box with x-coordinate between x1 and x2 and y-coordinate between y1 and y2
def randomized_click(x1, x2, y1, y2):
    return randint(x1, x2), randint(y1, y2)


# Adds a margin between x-coordinates x1 and x2 as well as between y-coordinates y1 and y2
def add_margin(x1, x2, y1, y2, margin):
    # In case margin is too big, return original coordinates
    if x2 - x1 <= margin*2 or y2 - y1 <= margin*2:
        return x1, x2, y1, y2
    return x1 + margin, x2 - margin, y1 + margin, y2 - margin


# Start a stopwatch displayed in the application window when a script is started
def start_stopwatch(android):
    start_time = int(time.time())
    while True:
        time_past = int(time.time()) - start_time

        if android.script_stopped:
            android.stopwatch_label["text"] = "0:00:00"
            return

        # Nicely format and display the time on the stopwatch
        hours = time_past // 3600
        if (time_past // 60) % 60 < 10:
            minutes = f"0{(time_past // 60) % 60}"
        else:
            minutes = (time_past // 60) % 60

        if time_past % 60 < 10:
            seconds = f"0{time_past % 60}"
        else:
            seconds = time_past % 60

        android.stopwatch_label["text"] = f"{hours}:{minutes}:{seconds}"

        time.sleep(1)
