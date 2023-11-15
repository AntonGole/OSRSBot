import threading
from pyautogui import *
from pynput.keyboard import Listener, Controller, Key
from tkinter import *
import win32gui
from desktopmagic.screengrab_win32 import getRectAsImage


def input_thread(coordinateString, window_title):
    # Handling on keypress and on keyrelease event
    def on_press(key):
        print("Key pressed: " + str(key))

        if str(key) == "Key.up":
            move(0, -1)
        elif str(key) == "Key.down":
            move(0, 1)
        elif str(key) == "Key.right":
            move(1, 0)
        elif str(key) == "Key.left":
            move(-1, 0)

        elif str(key) == "Key.ctrl_l":
            window_handle = win32gui.FindWindow(None, window_title)
            x, y, x1, x2 = win32gui.GetWindowRect(window_handle)
            if not coordinateString:
                print("Top left corner calibrated!")
                coordinateString.append(str(position().x - x - 459))
                coordinateString.append(str(position().y - y - 164))
            else:
                coordinateString.append(str(position().x - x - 459))
                coordinateString.append(str(position().y - y - 164))
                print("Bottom right corner calibrated!")
                r = Tk()
                r.withdraw()
                r.clipboard_clear()
                print(f"x1, x2, y1, y2 = add_margin({coordinateString[0]}, {coordinateString[2]}, {coordinateString[1]}, {coordinateString[3]}, 3)")
                r.clipboard_append(f"x1, x2, y1, y2 = add_margin({coordinateString[0]}, {coordinateString[2]}, {coordinateString[1]}, {coordinateString[3]}, 3)")
                r.update()
                quit()
        elif str(key) == "Key.ctrl_r":
            window_handle = win32gui.FindWindow(None, window_title)
            x, y, x1, x2 = win32gui.GetWindowRect(window_handle)
            img = screenshot_region(x, y, x1, x2)
            pix = img.load()
            print(f"add_color_margin(pix[{str(position().x - x - 459)}, {str(position().y - y - 164)}], {pix[position().x - x, position().y - y][0]}, {pix[position().x - x, position().y - y][1]}, {pix[position().x - x, position().y - y][2]}, {0})")
            print(f"wait_step(android, {str(position().x - x - 459)}, {str(position().y - y - 164)}, ({pix[position().x - x, position().y - y][0]}, {pix[position().x - x, position().y - y][1]}, {pix[position().x - x, position().y - y][2]}), margin, timeout)")

    def on_release(key):
        pass

    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()


def screenshot_region(x, y, x1, x2):
    return getRectAsImage((x, y, x1, x2))


def print_coordinates(window_title):
    timer = threading.Timer(1, print_coordinates, [window_title])
    timer.daemon = True
    window_handle = win32gui.FindWindow(None, window_title)
    x, y, x1, x2 = win32gui.GetWindowRect(window_handle)

    timer.start()
    print(position().x - x - 459)
    print(position().y - y - 164)
    print()

    img = screenshot_region(x, y, x1, x2)
    pix = img.load()
    try:
        print(pix[position().x - x, position().y - y])
    except:
        print("Unable to print coordinates of mouse")
