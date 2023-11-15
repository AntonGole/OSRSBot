import os
import random
import threading
from random import *
import time
from tkinter import PhotoImage

import PIL
from PIL import Image, ImageTk
from pyautogui import sleep


def cmd(command):
    os.system(command)


def randomized_click(x1, x2, y1, y2):
    return randint(x1, x2), randint(y1, y2)


def randomized_gauss_click(x1, x2, y1, y2):
    while True:
        x = gauss((x1 + x2) / 2, max(x1, x2) - min(x1, x2) * 0.25)
        if x1 < x < x2:
            break
    while True:
        y = gauss((y1 + y2) / 2, max(y1, y2) - min(y1, y2) * 0.25)
        if y1 < y < y2:
            return x, y


def randomized_swipe(y1):
    y1 = randint(y1, y1 + 200)
    y2 = y1 + randint(150, 350)
    return randint(400, 700), randint(y1, y2)


def add_margin(x1, x2, y1, y2, margin):
    return x1 + margin, x2 - margin, y1 + margin, y2 - margin


def add_color_margin(pix, pix_0_value, pix_1_value, pix_2_value, margin):
    if ((pix_0_value - margin) < pix[0] < (pix_0_value + margin)) and \
            ((pix_1_value - margin) < pix[1] < (pix_1_value + margin)) and \
            ((pix_2_value - margin) < pix[2] < (pix_2_value + margin)):
        return True
    return False


def find_square():
    img = PIL.Image.open(f"images/map-marker-icon2x.png")

    for x in range(img.height):
        for y in range(img.width):
            if not img.getpixel((x, y)) == (2, 2, 2):
                img.putpixel((x, y), (0, 162, 232))

    img.save("images/map-marker-icon2x.png")


def update_timer(login_time, android):
    logout_time = int(time.time()) + login_time

    while True:
        time_left = logout_time - int(time.time())

        if android.script_stopped:
            android.time_label["text"] = "0:00:00"
            return
        if time_left <= 0:
            return

        hours = time_left // 3600
        if (time_left // 60) % 60 < 10:
            minutes = f"0{(time_left // 60) % 60}"
        else:
            minutes = (time_left // 60) % 60

        if time_left % 60 < 10:
            seconds = f"0{time_left % 60}"
        else:
            seconds = time_left % 60

        android.time_label["text"] = f"{hours}:{minutes}:{seconds}"

        time.sleep(1)


def stopwatch(android):
    start_time = int(time.time())
    while True:
        time_past = int(time.time()) - start_time

        if android.script_stopped:
            android.stopwatch_label["text"] = "0:00:00"
            return

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


def screenshot_loop(gui, android, index):
    while True:
        time.sleep(30)
        cmd(f"vboxmanage controlvm \"{android.name}\" screenshotpng label_images/{android.name[-1]}.png")
        img = Image.open(f"label_images/{android.name[-1]}.png")
        img = img.resize((229, 172), Image.ANTIALIAS)
        #img = img.resize((512, 382), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(img)

        gui.image_labels[index].configure(image=new_image)
        gui.image_labels[index].image = new_image
        os.remove(f"label_images/{android.name[-1]}.png")


# Function for waiting for a step to be done, should be implemented into every step.
# Implements a timeout, where if the timeout limit is reached, the function will return True
# For this to work correctly the script must have a way to reset to step 1, so that if this function
# returns True the script will jump back to the start and reset
def wait_step(android, x, y, rgb, margin, timeout):
    start_time = int(time.time())
    while True:
        sleep(0.1)

        time_past = int(time.time()) - start_time
        if time_past >= timeout:
            print("Timeout! Resetting script")
            return True

        pix = android.screenshot()
        if add_color_margin(pix[x, y], rgb[0], rgb[1], rgb[2], margin):
            sleep(randint(350, 450) / 1000)
            return False
