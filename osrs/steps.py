import sys

import numpy as np

from Util.helpers import *
from pyautogui import *


def OSRS_click_myths_bank(android):
    x1, x2, y1, y2 = add_margin(497, 520, 389, 405, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_click_myths_range(android):
    x1, x2, y1, y2 = add_margin(470, 487, 360, 387, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_deposit_item(android, t1, t2):
    x1, x2, y1, y2 = add_margin(586, 626, 608, 648, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_withdraw_item(android, t1, t2):
    x1, x2, y1, y2 = add_margin(567, 608, 571, 605, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_withdraw_item_1(android, t1, t2):
    x1, x2, y1, y2 = add_margin(567, 608, 571, 605, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_withdraw_item_2(android, t1, t2):
    x1, x2, y1, y2 = add_margin(567, 608, 530, 566, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_withdraw_item_3(android, t1, t2):
    x1, x2, y1, y2 = add_margin(567, 608, 490, 526, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_click_quantity_1(android, t1, t2):
    x1, x2, y1, y2 = add_margin(357, 377, 630, 647, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_click_quantity_all(android, t1, t2):
    x1, x2, y1, y2 = add_margin(470, 492, 629, 645, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_click_item_13(android):
    x1, x2, y1, y2 = add_margin(760, 795, 467, 503, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_click_item_17(android, t1, t2):
    x1, x2, y1, y2 = add_margin(760, 795, 508, 544, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_wait_bank_open(android):
    print(f"Waiting for bank open! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[36, 573], 251, 182, 30, 10)):
            print(f"Bank clicked! {android.name}")
            break


def OSRS_wait_bank_open_2(android):
    print(f"Waiting for bank open! {android.name}")
    tries = 0
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[36, 573], 251, 182, 30, 10)):
            print(f"Bank clicked! {android.name}")
            break
        tries += 1
        if tries == 150:
            OSRS_blast_furnace_bank(android)
            tries = 0


def OSRS_wait_click_range(android):
    print(f"Waiting for range clicked! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (pix[532, 22] == (0, 0, 0)):
            print(f"Range clicked! {android.name}")
            break


def OSRS_wait_logout(android, manual):
    print(f"Waiting logout! {android.name}")
    while True:
        if android.script_stopped and not manual:
            android.status_label["text"] = "Stopped"
            exit(0)
        sleep(0.1)
        pix = android.screenshot()
        if not (pix[532, 22] == (0, 0, 0)):
            print(f"Logged out! {android.name}")
            break
    if android.script_stopped and not manual:
        android.status_label["text"] = "Stopped"
        exit(0)


def OSRS_wait_login_1(android, manual):
    print(f"Waiting login step 1/2! {android.name}")
    while True:
        if android.script_stopped and not manual:
            android.status_label["text"] = "Stopped"
            exit(0)
        sleep(0.1)
        pix = android.screenshot()
        if pix[386, 325] == (0, 0, 0):
            print(f"Logged in step 1/2! {android.name}")
            break
    if android.script_stopped and not manual:
        android.status_label["text"] = "Stopped"
        exit(0)


def OSRS_wait_login_2(android, manual):
    print(f"Waiting login step 2/2! {android.name}")
    while True:
        if android.script_stopped and not manual:
            android.status_label["text"] = "Stopped"
            exit(0)
        sleep(0.1)
        pix = android.screenshot()
        if not (pix[386, 325] == (0, 0, 0)):
            print(f"Logged in step 2/2! {android.name}")
            break
    if android.script_stopped and not manual:
        android.status_label["text"] = "Stopped"
        exit(0)


def OSRS_click_guild_range(android):
    x1, x2, y1, y2 = add_margin(590, 607, 324, 362, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_click_guild_bank_first(android):
    x1, x2, y1, y2 = add_margin(459, 479, 377, 390, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_click_guild_bank(android):
    x1, x2, y1, y2 = add_margin(386, 406, 392, 413, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_click_compass(android, t1, t2):
    x1, x2, y1, y2 = add_margin(809, 834, 8, 28, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)
    return clickX, clickY


def OSRS_click_look_west(android, lastX, lastY, t1, t2):
    x1, x2, y1, y2 = add_margin(lastX - 35, lastX + 35, lastY + 118, lastY + 139, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_click_look_south(android, lastX, lastY, t1, t2):
    x1, x2, y1, y2 = add_margin(lastX - 35, lastX + 35, lastY + 89, lastY + 112, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(t1, t2) / 1000)


def OSRS_toggle_mode(android, t1, t2, on):
    x1, x2, y1, y2 = add_margin(15, 52, 286, 309, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    if on:
        OSRS_wait_toggle_on(android)
    else:
        OSRS_wait_toggle_off(android)
    sleep(randint(t1, t2) / 1000)


def OSRS_wait_toggle_on(android):
    print(f"Waiting for toggle on! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[45, 305], 254, 203, 101, 10):
            print(f"Toggle on! {android.name}")
            break


def OSRS_wait_toggle_off(android):
    print(f"Waiting for toggle off! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[45, 305], 254, 203, 101, 10)):
            print(f"Toggle off! {android.name}")
            break


def OSRS_click_varrock_bank(android):
    x1, x2, y1, y2 = add_margin(498, 528, 369, 388, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def sleep_with_checks(android, sleep_time):
    sleep_end = time.time() + sleep_time

    while time.time() < sleep_end:
        if android.script_stopped:
            android.status_label["text"] = "Stopped"
            exit(0)
        sleep(1)


# Fishing karambwans functions
def OSRS_click_teleport_house(android):
    x1, x2, y1, y2 = add_margin(135, 155, 419, 441, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_teleport_house(android)
    sleep(randint(150, 250) / 1000)


# For making planks script
def OSRS_click_teleport_house_3(android):
    x1, x2, y1, y2 = add_margin(135, 155, 419, 441, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(300, 600) / 1000)
    android.input_press("KEYCODE_F10", 50, 150)
    OSRS_wait_click_teleport_house(android)
    sleep(randint(150, 250) / 1000)


def OSRS_click_teleport_house_2(android):
    x1, x2, y1, y2 = add_margin(135, 155, 419, 441, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_teleport_house_2(android)
    sleep(randint(150, 250) / 1000)


def OSRS_wait_click_teleport_house(android):
    print(f"Waiting for teleport to house! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[326, 238], 92, 44, 36, 10):
            print(f"Teleported to house! {android.name}")
            break


def OSRS_wait_click_teleport_house_2(android):
    print(f"Waiting for teleport to house! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[472, 140], 101, 16, 11, 10):
            print(f"Teleported to house! {android.name}")
            break


def OSRS_click_poh_fairy_ring(android):
    x1, x2, y1, y2 = add_margin(470, 502, 228, 257, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(300, 800) / 1000)
    return clickX, clickY


def OSRS_click_last_destination(android, lastX, lastY):
    x1, x2, y1, y2 = add_margin(lastX - 30, lastX + 30, lastY + 87, lastY + 113, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_last_destination(android)
    sleep(randint(300, 800) / 1000)


def OSRS_wait_click_last_destination(android):
    print(f"Waiting for click last destination! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[977, 87], 87, 108, 156, 10):
            print(f"Teleported to last destination! {android.name}")
            break


def OSRS_click_fishing_spot(android):
    x1, x2, y1, y2 = add_margin(672, 691, 378, 393, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_wait_interface_open(android):
    print(f"Waiting for interface open! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (pix[532, 22] == (0, 0, 0)):
            print(f"Interface open! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_wait_interface_open_2(android):
    print(f"Waiting for interface open! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[592, 15], 85, 27, 26, 5)):
            print(f"Interface open! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_close_interface(android):
    x1, x2, y1, y2 = add_margin(264, 360, 119, 136, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_interface_close(android)


def OSRS_wait_interface_close(android):
    print(f"Waiting for interface close! {android.name}")
    tries_2 = 0
    while True:
        sleep(0.1)
        tries = 0
        if tries >= 100:
            x1, x2, y1, y2 = add_margin(264, 360, 119, 136, 3)
            clickX, clickY = randomized_click(x1, x2, y1, y2)
            android.input_tap(clickX, clickY)
            tries = 0
            tries_2 += 1
            if tries_2 > 2:
                sys.exit(0)
        pix = android.screenshot()
        if pix[532, 22] == (0, 0, 0):
            print(f"Interface close! {android.name}")
            sleep(randint(50, 150) / 1000)
            break
        tries += 1


def OSRS_wait_interface_close_2(android):
    print(f"Waiting for interface close! {android.name}")
    tries_2 = 0
    tries = 0
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[592, 15], 85, 27, 26, 5):
            print(f"Interface close! {android.name}")
            sleep(randint(50, 150) / 1000)
            break
        tries += 1
        if tries == 50:
            android.input_press("KEYCODE_SPACE", 0, 0)
            tries = 0
            tries_2 += 1
            if tries_2 > 3:
                sys.exit(0)


def OSRS_click_crafting_cape(android):
    x1, x2, y1, y2 = add_margin(786, 820, 387, 421, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(50, 150) / 1000)
    return clickX, clickY


def OSRS_teleport_crafting_guild(android, lastX, lastY):
    x1, x2, y1, y2 = add_margin(lastX - 30, lastX + 30, lastY + 87, lastY + 113, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_teleport_crafting_guild(android)
    sleep(randint(50, 150) / 1000)


# For making planks script
def OSRS_teleport_crafting_guild_2(android, lastX, lastY):
    x1, x2, y1, y2 = add_margin(lastX - 30, lastX + 30, lastY + 87, lastY + 113, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(300, 600) / 1000)
    android.input_press("KEYCODE_F3", 50, 150)
    OSRS_wait_teleport_crafting_guild(android)
    sleep(randint(50, 150) / 1000)


def OSRS_wait_teleport_crafting_guild(android):
    print(f"Waiting for teleport crafting guild! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[704, 521], 176, 176, 163, 10):
            print(f"Teleported to crafting guild! {android.name}")
            break


def OSRS_teleport_crafting_guild_north(android, lastX, lastY):
    x1, x2, y1, y2 = add_margin(lastX - 30, lastX + 30, lastY + 87, lastY + 113, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_teleport_crafting_guild_north(android)
    sleep(randint(50, 150) / 1000)


def OSRS_wait_teleport_crafting_guild_north(android):
    print(f"Waiting for teleport crafting guild! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[857, 129], 70, 93, 130, 25):
            print(f"Teleported to crafting guild! {android.name}")
            break


def OSRS_click_crafting_guild_bank(android):
    x1, x2, y1, y2 = add_margin(339, 357, 502, 520, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    return clickX, clickY


def OSRS_click_crafting_guild_bank_north(android):
    x1, x2, y1, y2 = add_margin(643, 665, 534, 549, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    return clickX, clickY


def OSRS_agility_falador_obstacle_1(android):
    x1, x2, y1, y2 = add_margin(665, 675, 218, 227, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 1")
    return clickX, clickY


def OSRS_agility_falador_obstacle_2(android):
    x1, x2, y1, y2 = add_margin(603, 624, 346, 368, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 2")
    return clickX, clickY


def OSRS_agility_falador_obstacle_3(android):
    x1, x2, y1, y2 = add_margin(566, 590, 238, 281, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 3")
    return clickX, clickY


def OSRS_agility_falador_obstacle_4(android):
    x1, x2, y1, y2 = add_margin(450, 473, 328, 350, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 4")
    return clickX, clickY


def OSRS_agility_falador_obstacle_5(android):
    x1, x2, y1, y2 = add_margin(401, 421, 349, 401, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 5")
    return clickX, clickY


def OSRS_agility_falador_obstacle_6(android):
    x1, x2, y1, y2 = add_margin(327, 350, 357, 383, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 6")
    return clickX, clickY


def OSRS_agility_falador_obstacle_7(android):
    x1, x2, y1, y2 = add_margin(447, 468, 398, 424, 5)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 7")
    return clickX, clickY


def OSRS_agility_falador_obstacle_8(android):
    x1, x2, y1, y2 = add_margin(402, 461, 386, 403, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 8")
    return clickX, clickY


def OSRS_agility_falador_obstacle_9(android):
    x1, x2, y1, y2 = add_margin(411, 446, 457, 493, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 9")
    return clickX, clickY


def OSRS_agility_falador_obstacle_10(android):
    x1, x2, y1, y2 = add_margin(438, 488, 436, 466, 6)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 10")
    return clickX, clickY


def OSRS_agility_falador_obstacle_11(android):
    x1, x2, y1, y2 = add_margin(521, 550, 559, 590, 6)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 11")
    return clickX, clickY


def OSRS_agility_falador_obstacle_12(android):
    x1, x2, y1, y2 = add_margin(556, 594, 383, 421, 6)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 12")
    return clickX, clickY


def OSRS_agility_falador_obstacle_13(android):
    x1, x2, y1, y2 = add_margin(608, 667, 379, 418, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 13")
    return clickX, clickY


def OSRS_wait_obstacle_done(android, last_pixel_count):
    waited = 0
    while True:
        sleep(0.2)
        pix = android.screenshot()
        new_pixel_count = 0
        for x in range(930, 956):
            for y in range(417, 431):
                if pix[x, y] != (255, 255, 160):
                    new_pixel_count += 1
        if new_pixel_count != last_pixel_count:
            print("New pixel count sent: " + str(new_pixel_count))
            return new_pixel_count

        waited += 1
        if waited == 15:
            print("Maximum wait duration reached, continuing")
            return new_pixel_count
        if waited % 15 == 0:
            print("Last pixel count: " + str(last_pixel_count))
            print("New pixel count: " + str(new_pixel_count))
            print()


def OSRS_wait_obstacle_done_3(android, last_pixels):
    while True:
        sleep(0.05)
        pix = android.screenshot()
        new_pixels = []
        for x in range(976, 1003):
            for y in range(427, 440):
                new_pixels.append(pix[x, y])
        new_pixels.sort()
        if new_pixels != last_pixels:
            return new_pixels


# def OSRS_wait_obstacle_done_2(android, last_pixels):
#     waited = 0
#     while True:
#         sleep(0.2)
#         pix = android.screenshot()
#         new_pixels = []
#         for x in range(726, 749):
#             for y in range(45, 56):
#                 new_pixels.append(pix[x, y])
#         new_pixels.sort()
#         if new_pixels != last_pixels:
#             return new_pixels
#
#         waited += 1
#         if waited == 125:
#             print("Maximum wait duration reached, teleporting back to seers")
#             return 0


def OSRS_wait_obstacle_done_2(android, last_pixels):
    tries = 0
    while True:
        sleep(0.05)
        pix = android.screenshot()
        new_pixels = []
        for x in range(726, 749):
            for y in range(45, 56):
                new_pixels.append(pix[x, y])
        new_pixels.sort()
        if new_pixels != last_pixels:
            return new_pixels
        if tries > 500:
            return 0
        tries += 1


def OSRS_wait_xp_drop(android, last_pixels):
    tries = 0
    while True:
        sleep(0.05)
        pix = android.screenshot()
        new_pixels = []
        for x in range(726, 749):
            for y in range(45, 56):
                if add_color_margin(pix[x, y], 200, 200, 200, 30):
                    new_pixels.append(pix[x, y])
        new_pixels.sort()
        if new_pixels != last_pixels:
            return new_pixels
        if tries > 500:
            return 0
        tries += 1


def count_pixels(android):
    pix = android.screenshot()
    pixels = []
    for x in range(726, 749):
        for y in range(45, 56):
            pixels.append(pix[x, y])
    pixels.sort()
    return pixels


def count_pixels_improved(android):
    pix = android.screenshot()
    pixels = []
    for x in range(726, 749):
        for y in range(45, 56):
            if add_color_margin(pix[x, y], 200, 200, 200, 30):
                pixels.append(pix[x, y])
    pixels.sort()
    return pixels


def count_pixels_2(android):
    pix = android.screenshot()
    pixels = []
    for x in range(976, 1003):
        for y in range(427, 440):
            pixels.append(pix[x, y])
    pixels.sort()
    return pixels


def count_pixels_disc(android):
    pix = android.screenshot()
    new_pixel_count = 0
    for x in range(930, 956):
        for y in range(417, 431):
            if pix[x, y] != (255, 255, 160):
                new_pixel_count += 1

    return new_pixel_count


def find_pixels(android):
    while True:
        pix = android.screenshot()
        total = 0
        top_most = 2000
        bot_most = 0
        left_most = 2000
        right_most = 0
        for x in range(520, 640):
            for y in range(230, 315):
                if add_color_margin(pix[x, y], 122, 127, 120, 4):
                    # print(x, y)
                    if x > right_most:
                        right_most = x
                    elif x < left_most:
                        left_most = x
                    if y < top_most:
                        top_most = y
                    elif y > bot_most:
                        bot_most = y
                    total += 1
        if total == 0:
            print("No right values found, trying again")
            sleep(1)
            continue
        else:
            break
    # print(total)
    return left_most, right_most, top_most, bot_most


def find_pixels_2(android):
    while True:
        pix = android.screenshot()
        total = 0
        top_most = 2000
        bot_most = 0
        left_most = 2000
        right_most = 0
        for x in range(520, 640):
            for y in range(230, 315):
                if add_color_margin(pix[x, y], 96, 125, 86, 4):
                    # print(x, y)
                    if x > right_most:
                        right_most = x
                    elif x < left_most:
                        left_most = x
                    if y < top_most:
                        top_most = y
                    elif y > bot_most:
                        bot_most = y
                    total += 1
        if total == 0:
            print("No right values found, trying again")
            sleep(1)
            continue
        else:
            break
    # print(total)
    return left_most, right_most, top_most, bot_most


def OSRS_agility_seers_obstacle_1(android):
    left, right, top, bot = find_pixels_2(android)
    print(left, right, top, bot)
    clickX, clickY = randomized_click(left, right, top, bot)
    android.input_tap(clickX, clickY)
    print(clickX, clickY)
    print("Clicked obstacle 1")
    return clickX, clickY


def OSRS_agility_seers_obstacle_2(android):
    # Made Y level 20 less marginal for panning of camera
    x1, x2, y1, y2 = add_margin(297, 322, 316, 347, 5)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 2")
    return clickX, clickY


def OSRS_agility_seers_obstacle_3(android):
    x1, x2, y1, y2 = add_margin(419, 444, 502, 526, 5)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 3")
    return clickX, clickY


def OSRS_agility_seers_obstacle_4(android):
    # Made Y level 15 less marginal for panning of camera
    x1, x2, y1, y2 = add_margin(488, 608, 482, 493, 5)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 4")
    return clickX, clickY


def OSRS_agility_seers_obstacle_5(android):
    x1, x2, y1, y2 = add_margin(294, 337, 445, 477, 8)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 5")
    return clickX, clickY


def OSRS_agility_seers_obstacle_6(android):
    x1, x2, y1, y2 = add_margin(527, 557, 379, 464, 5)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 6")
    return clickX, clickY


def OSRS_click_teleport_seers(android):
    x1, x2, y1, y2 = add_margin(220, 247, 417, 441, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_teleport_seers(android)
    sleep(randint(300, 500) / 1000)


def OSRS_wait_click_teleport_seers(android):
    print(f"Waiting for teleport to seers! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[392, 529], 84, 80, 70, 6)):
            print(f"Teleported to seers! {android.name}")
            break


def OSRS_agility_ardy_obstacle_1(android):
    x1, x2, y1, y2 = add_margin(365, 392, 390, 407, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 1")


def OSRS_agility_ardy_obstacle_2(android):
    x1, x2, y1, y2 = add_margin(516, 538, 685, 723, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 2")


def OSRS_agility_ardy_obstacle_3(android):
    x1, x2, y1, y2 = add_margin(597, 618, 386, 396, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 3")


def OSRS_agility_ardy_pick_up_marks(android):
    x1, x2, y1, y2 = add_margin(485, 498, 383, 395, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Picked up marks!")


def OSRS_agility_ardy_obstacle_4(android):
    x1, x2, y1, y2 = add_margin(578, 603, 348, 375, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 4")


def OSRS_agility_ardy_obstacle_5(android):
    x1, x2, y1, y2 = add_margin(504, 524, 264, 282, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 5")


def OSRS_agility_ardy_obstacle_6(android):
    x1, x2, y1, y2 = add_margin(445, 466, 211, 226, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 6")


def OSRS_agility_ardy_obstacle_7(android):
    x1, x2, y1, y2 = add_margin(485, 509, 354, 387, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Clicked obstacle 7")


def OSRS_click_house_options(android):
    x1, x2, y1, y2 = add_margin(855, 893, 539, 577, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_house_options(android)
    sleep(randint(300, 400) / 1000)


def OSRS_wait_click_house_options(android):
    print(f"Waiting for clicked house options! {android.name}")
    tries = 0
    while True:
        sleep(0.1)
        tries += 1
        pix = android.screenshot()
        if not (add_color_margin(pix[36, 575], 236, 158, 13, 6)):
            print("Clicked house options!")
            break
        if tries > 100:
            print("Reached 100 tries!")
            break


def OSRS_click_call_servant(android):
    x1, x2, y1, y2 = add_margin(782, 918, 537, 566, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    #OSRS_wait_interface_open(android)
    OSRS_wait_call_servant(android)
    sleep(randint(150, 250) / 1000)


def OSRS_wait_call_servant(android):
    print(f"Waiting for servant! {android.name}")
    tries = 0
    tries_2 = 0
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (pix[532, 22] == (0, 0, 0)):
            print(f"Servant arrived! {android.name}")
            sleep(randint(20, 50) / 1000)
            break
        tries += 1
        if tries == 40:
            print("Maximum amount of servant tries reached, trying again!")
            OSRS_click_call_servant(android)
            tries = 0
            tries_2 += 1
            if tries_2 > 2:
                sys.exit(0)


def OSRS_wait_next_dialog(android, is_option):
    if is_option:
        while True:
            sleep(0.1)
            pix = android.screenshot()
            if not (add_color_margin(pix[94, 86], 178, 163, 132, 6)):
                print("Clicked option!")
                sleep(randint(50, 100) / 1000)
                break

    else:
        while True:
            sleep(0.1)
            pix = android.screenshot()
            if add_color_margin(pix[94, 86], 178, 163, 132, 6):
                print("Continued dialog!")
                sleep(randint(50, 100) / 1000)
                break


def OSRS_make_myth_rack_1(android):
    x1, x2, y1, y2 = add_margin(455, 515, 412, 440, 6)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Step 1 done!")
    sleep(randint(50, 100) / 1000)
    return clickX, clickY


def OSRS_make_myth_rack_2(android, lastX, lastY):
    x1, x2, y1, y2 = add_margin(lastX - 30, lastX + 30, lastY + 87, lastY + 113, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_construction_popup_open(android)
    print("Step 2 done!")


def OSRS_wait_construction_popup_open(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[659, 469], 93, 81, 60, 6):
            print("Cons popup opened!")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_wait_construction_popup_close(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[659, 469], 93, 81, 60, 6)):
            print("Cons popup closed!")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_wait_myth_rack_built(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[516, 436], 192, 183, 182, 10):
            print("Myth rack built!")
            sleep(randint(50, 250) / 1000)
            break


def OSRS_make_myth_rack_5(android, lastX, lastY):
    x1, x2, y1, y2 = add_margin(lastX - 30, lastX + 30, lastY + 114, lastY + 140, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Step 5 done!")
    sleep(randint(50, 250) / 1000)


def OSRS_click_poh_pendant(android):
    x1, x2, y1, y2 = add_margin(575, 594, 300, 322, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_poh_pendant(android)
    sleep(randint(250, 400) / 1000)


def OSRS_wait_click_poh_pendant(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[625, 13], 0, 0, 0, 2)):
            print("Poh pendant clicked!")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_find_barge_guard(android):
    pix = android.screenshot()
    clickX = 1024
    clickY = 0
    for x in range(847, 990):
        for y in range(41, 143):
            if add_color_margin(pix[x, y], 75, 90, 138, 30):
                if y > clickY:
                    clickY = y
                if x < clickX:
                    clickX = x

    print(clickX, clickY)
    clickX, clickY = randomized_click(clickX, clickX + 20, clickY + 17, clickY + 30)
    android.input_tap(clickX, clickY)

    sleep(randint(7000, 7500) / 1000)

    pix = android.screenshot()
    coordinates = []
    for x in range(570, 760):
        for y in range(270, 430):
            if add_color_margin(pix[x, y], 52, 19, 13, 3):
                coordinates.append((x, y))

    if not coordinates:
        return True
    coord = choice(coordinates)
    clickX = coord[0]
    clickY = coord[1]
    android.input_tap(clickX, clickY)
    lastX = clickX
    lastY = clickY

    sleep(randint(50, 250) / 1000)

    x1, x2, y1, y2 = add_margin(lastX - 30, lastX + 30, lastY + 87, lastY + 113, 4)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)

    if wait_step(android, 64, 87, (133, 130, 60), 8, 60):
        return True

    print("Barge guard clicked!")
    return False


def OSRS_click_hole(android):
    x1, x2, y1, y2 = add_margin(308, 352, 194, 215, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_hole(android)
    sleep(randint(250, 400) / 1000)


def OSRS_wait_click_hole(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[555, 293], 200, 156, 87, 6):
            print("Hole clicked!")
            sleep(randint(150, 350) / 1000)
            break


def OSRS_click_tree_1(android):
    x1, x2, y1, y2 = add_margin(379, 427, 311, 354, 8)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_tree_1(android)
    sleep(randint(250, 400) / 1000)


def OSRS_wait_click_tree_1(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[464, 365], 202, 158, 88, 6):
            sleep(randint(150, 350) / 1000)
            break


def OSRS_wait_click_tree_1_chopped(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()

        if add_color_margin(pix[921, 615], 157, 121, 62, 8):
            print(f"Inventory full! {android.name}")
            sleep(randint(50, 300) / 1000)
            return 1

        if not (pix[532, 22] == (0, 0, 0)):
            print(f"Interface open! {android.name}")
            while True:
                android.input_press("KEYCODE_SPACE", 800, 1500)
                sleep(randint(50, 300) / 1000)
                if pix[532, 22] == (0, 0, 0):
                    return 1
                sleep(2)

        if not (add_color_margin(pix[444, 385], 147, 183, 80, 8)):
            sleep(randint(150, 350) / 1000)
            return 0


def OSRS_click_tree_2(android):
    x1, x2, y1, y2 = add_margin(595, 651, 303, 348, 8)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_tree_2(android)
    sleep(randint(250, 400) / 1000)


def OSRS_wait_click_tree_2(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[567, 333], 140, 175, 76, 8):
            sleep(randint(150, 350) / 1000)
            break


def OSRS_wait_click_tree_2_chopped(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()

        if add_color_margin(pix[922, 605], 163, 125, 66, 8):
            print(f"Inventory full! {android.name}")
            sleep(randint(50, 300) / 1000)
            return 1

        if not (pix[534, 23] == (0, 0, 0)):
            print(f"Interface open! {android.name}")
            tries = 0
            while True:
                android.input_press("KEYCODE_SPACE", 800, 1500)
                sleep(2)
                pix = android.screenshot()
                if pix[534, 23] == (0, 0, 0):
                    print("Returning 0 after pressing space")
                    return 0
                tries += 1
                if tries > 100:
                    sys.exit(0)

        if not (add_color_margin(pix[567, 333], 140, 175, 76, 8)):
            print("Tree 2 chopped!")
            sleep(randint(150, 350) / 1000)
            return 0


def OSRS_wait_tree_1_2_respawned(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[368, 379], 114, 143, 64, 8):
            print("Tree 1 respawned!")
            sleep(randint(350, 450) / 1000)
            break


def OSRS_click_tree_1_2(android):
    x1, x2, y1, y2 = add_margin(364, 417, 380, 433, 8)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Tree 1 clicked!")
    OSRS_wait_click_tree_1_2(android)
    sleep(randint(250, 400) / 1000)


def OSRS_wait_click_tree_1_2(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[444, 385], 147, 183, 80, 8):
            sleep(randint(150, 350) / 1000)
            break


def OSRS_wait_click_tree_1_2_chopped(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()

        if add_color_margin(pix[922, 605], 163, 125, 66, 6):
            print(f"Inventory full! {android.name}")
            sleep(randint(50, 300) / 1000)
            return 1

        if not (pix[534, 23] == (0, 0, 0)):
            print(f"Interface open! {android.name}")
            tries = 0
            while True:
                android.input_press("KEYCODE_SPACE", 800, 1500)
                sleep(2)
                pix = android.screenshot()
                if pix[534, 23] == (0, 0, 0):
                    print("Returning 0 after pressing space")
                    return 0
                tries += 1
                if tries > 100:
                    sys.exit(0)
        print(pix[444, 385])
        if not (add_color_margin(pix[444, 385], 147, 183, 80, 8)):
            print("Tree 1 chopped down!")
            sleep(randint(150, 350) / 1000)
            return 0


def OSRS_click_tree_2_1(android):
    x1, x2, y1, y2 = add_margin(597, 656, 341, 386, 8)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    print("Tree 2 clicked!")
    OSRS_wait_click_tree_2(android)
    sleep(randint(250, 400) / 1000)


def OSRS_wait_tree_2_1_respawned(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[645, 334], 149, 186, 81, 6):
            print("Tree 2 respawned!")
            sleep(randint(350, 450) / 1000)
            break


def OSRS_click_iron_ore_1(android):
    x1, x2, y1, y2 = add_margin(397, 593, 641, 741, 25)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(1)
    if OSRS_wait_iron_ore_1_mined(android):
        OSRS_drop_inventory(android)
    #sleep(randint(1780, 1820) / 1000)


def OSRS_wait_iron_ore_1_mined(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()

        if add_color_margin(pix[924, 609], 39, 17, 11, 10):
            print(f"Inventory full 1! {android.name}")
            sleep(randint(20, 100) / 1000)
            return 1

        if not (add_color_margin(pix[41, 81], 30, 21, 16, 10)):
            print(f"Interface open 1! {android.name}")
            while True:
                while True:
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    return 1

        if not (add_color_margin(pix[554, 653], 54, 31, 22, 10)):
            return 0


def OSRS_wait_iron_ore_1_respawned(android):
    while True:
        pix = android.screenshot()
        if add_color_margin(pix[554, 653], 54, 31, 22, 10):
            # OSRS_click_item(android, 1, 0, 10)
            # android.cooked_amount += 1
            # sleep(randint(0, 20) / 1000)
            break
        sleep(0.1)


def OSRS_click_iron_ore_2(android):
    x1, x2, y1, y2 = add_margin(171, 270, 443, 600, 25)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(1)
    if OSRS_wait_iron_ore_2_mined(android):
        OSRS_drop_inventory(android)
    #sleep(randint(1780, 1820) / 1000)


def OSRS_wait_iron_ore_2_mined(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()

        if add_color_margin(pix[924, 609], 39, 17, 11, 10):
            print(f"Inventory full 2! {android.name}")
            sleep(randint(50, 100) / 1000)
            return 1

        if not (add_color_margin(pix[41, 81], 30, 21, 16, 10)):
            print(f"Interface open 2! {android.name}")
            while True:
                android.input_press("KEYCODE_SPACE", 800, 1500)
                sleep(randint(300, 400) / 1000)
                android.input_press("KEYCODE_SPACE", 800, 1500)
                sleep(randint(300, 400) / 1000)
                android.input_press("KEYCODE_SPACE", 800, 1500)
                sleep(randint(300, 400) / 1000)
                android.input_press("KEYCODE_SPACE", 800, 1500)
                sleep(randint(300, 400) / 1000)
                android.input_press("KEYCODE_SPACE", 800, 1500)
                sleep(randint(300, 400) / 1000)
                return 1

        if not (add_color_margin(pix[349, 514], 38, 22, 17, 10)):
            return 0


def OSRS_wait_iron_ore_2_respawned(android):
    while True:
        pix = android.screenshot()
        if add_color_margin(pix[349, 514], 38, 22, 17, 10):
            # OSRS_click_item(android, 1, 0, 10)
            # android.cooked_amount += 1
            # sleep(randint(0, 20) / 1000)
            break
        sleep(0.1)


def OSRS_click_iron_ore_3(android):
    x1, x2, y1, y2 = add_margin(652, 731, 491, 620, 25)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    #sleep(1)
    # pix = android.screenshot()
    # if add_color_margin(pix[554, 653], 54, 31, 22, 10):
    #     OSRS_wait_iron_ore_3_mined(android)
    #     return True
    #if OSRS_wait_iron_ore_3_mined(android):
    #    OSRS_drop_inventory(android)
    sleep(randint(1790, 1850) / 1000)
    OSRS_click_item(android, 1, 20, 30)
    OSRS_click_item(android, 2, 20, 30)
    OSRS_click_item(android, 3, 20, 30)
    android.cooked_amount += 3


def OSRS_wait_iron_ore_3_mined(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()

        if add_color_margin(pix[924, 609], 39, 17, 11, 10):
            print(f"Inventory full 3! {android.name}")
            sleep(randint(50, 100) / 1000)
            return 1

        if not (add_color_margin(pix[41, 81], 30, 21, 16, 10)):
            print(f"Interface open 3! {android.name}")
            while True:
                while True:
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    android.input_press("KEYCODE_SPACE", 800, 1500)
                    sleep(randint(300, 400) / 1000)
                    return 1

        if not (add_color_margin(pix[675, 545], 45, 25, 18, 10)):
            return 0


def OSRS_wait_iron_ore_3_respawned(android):
    while True:
        pix = android.screenshot()
        if add_color_margin(pix[675, 545], 45, 25, 18, 10):
            # OSRS_click_item(android, 1, 0, 10)
            # android.cooked_amount += 1
            # sleep(randint(0, 20) / 1000)
            break
        sleep(0.1)


def OSRS_click_item(android, number, t1, t2):
    # Item 1
    if number == 1:
        x1, x2, y1, y2 = add_margin(763, 791, 345, 374, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 2
    elif number == 2:
        x1, x2, y1, y2 = add_margin(812, 839, 347, 374, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 3
    elif number == 3:
        x1, x2, y1, y2 = add_margin(859, 889, 346, 377, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 4
    elif number == 4:
        x1, x2, y1, y2 = add_margin(909, 937, 348, 377, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 5
    elif number == 5:
        x1, x2, y1, y2 = add_margin(761, 793, 389, 418, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 6
    elif number == 6:
        x1, x2, y1, y2 = add_margin(811, 842, 391, 418, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 7
    elif number == 7:
        x1, x2, y1, y2 = add_margin(858, 890, 389, 419, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 8
    elif number == 8:
        x1, x2, y1, y2 = add_margin(905, 937, 389, 418, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 9
    elif number == 9:
        x1, x2, y1, y2 = add_margin(762, 793, 431, 459, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 10
    elif number == 10:
        x1, x2, y1, y2 = add_margin(812, 843, 431, 458, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 11
    elif number == 11:
        x1, x2, y1, y2 = add_margin(862, 890, 431, 459, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 12
    elif number == 12:
        x1, x2, y1, y2 = add_margin(910, 938, 431, 460, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 13
    elif number == 13:
        x1, x2, y1, y2 = add_margin(765, 795, 473, 500, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 14
    elif number == 14:
        x1, x2, y1, y2 = add_margin(811, 841, 473, 501, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 15
    elif number == 15:
        x1, x2, y1, y2 = add_margin(857, 889, 472, 499, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 16
    elif number == 16:
        x1, x2, y1, y2 = add_margin(906, 939, 474, 500, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 17
    elif number == 17:
        x1, x2, y1, y2 = add_margin(764, 795, 515, 541, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 18
    elif number == 18:
        x1, x2, y1, y2 = add_margin(811, 841, 512, 541, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 19
    elif number == 19:
        x1, x2, y1, y2 = add_margin(859, 892, 513, 542, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 20
    elif number == 20:
        x1, x2, y1, y2 = add_margin(909, 939, 515, 542, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 21
    elif number == 21:
        x1, x2, y1, y2 = add_margin(763, 796, 554, 583, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 22
    elif number == 22:
        x1, x2, y1, y2 = add_margin(810, 843, 554, 581, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 23
    elif number == 23:
        x1, x2, y1, y2 = add_margin(860, 891, 556, 582, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 24
    elif number == 24:
        x1, x2, y1, y2 = add_margin(908, 941, 556, 583, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 25
    elif number == 25:
        x1, x2, y1, y2 = add_margin(763, 795, 596, 625, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 26
    elif number == 26:
        x1, x2, y1, y2 = add_margin(811, 842, 596, 626, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 27
    elif number == 27:
        x1, x2, y1, y2 = add_margin(859, 892, 596, 624, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)

    # Item 28
    elif number == 28:
        x1, x2, y1, y2 = add_margin(906, 942, 596, 624, 3)
        clickX, clickY = randomized_click(x1, x2, y1, y2)
        android.input_tap(clickX, clickY)
        sleep(randint(t1, t2) / 1000)


def OSRS_click_item_1(android):
    x1, x2, y1, y2 = add_margin(763, 791, 345, 374, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(50, 150) / 1000)


def OSRS_click_item_2(android):
    x1, x2, y1, y2 = add_margin(812, 839, 347, 374, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(50, 150) / 1000)


def OSRS_click_item_5(android):
    x1, x2, y1, y2 = add_margin(761, 793, 389, 418, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(50, 150) / 1000)


def OSRS_click_item_6(android):
    x1, x2, y1, y2 = add_margin(811, 842, 391, 418, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(50, 150) / 1000)


def OSRS_wait_fletching_done_myths(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[919, 606], 62, 65, 46, 10):
            sleep(randint(150, 350) / 1000)
            break


def OSRS_click_redwood_tree(android):
    x1, x2, y1, y2 = add_margin(244, 536, 53, 186, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_redwood_tree_chopped(android)


def OSRS_wait_redwood_tree_chopped(android):
    start_time = int(time.time())
    random_time = randint(120, 240)
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[313, 174], 51, 27, 20, 4)):
            sleep(randint(150, 350) / 1000)
            print("Redwood tree chopped!")
            break
        if OSRS_check_redwood_inventory_full(android):
            OSRS_click_item_2(android)
            OSRS_click_item_6(android)
            OSRS_wait_interface_open_2(android)
            sleep(randint(150, 350) / 1000)
            android.input_press("KEYCODE_1", 0, 0)
            OSRS_wait_redwood_inventory_done(android)
            OSRS_click_redwood_tree(android)
        if (int(time.time()) - start_time) > random_time:
            OSRS_click_redwood_tree(android)
            start_time = int(time.time())
            random_time = randint(120, 240)


def OSRS_check_redwood_tree_respawned(android):
    sleep(0.1)
    pix = android.screenshot()
    if add_color_margin(pix[313, 174], 51, 27, 20, 4):
        sleep(randint(150, 350) / 1000)
        print("Redwood tree respawned!")
        return 1
    return 0


def OSRS_check_redwood_inventory_full(android):
    sleep(0.1)
    pix = android.screenshot()
    if add_color_margin(pix[922, 605], 77, 34, 1, 10):
        sleep(randint(150, 350) / 1000)
        print("Redwood inventory full!")
        return 1
    return 0


def OSRS_wait_redwood_inventory_done(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[922, 605], 77, 34, 1, 10)):
            sleep(randint(150, 350) / 1000)
            print("Redwood inventory done!")
            break


def OSRS_click_edge_furnace(android):
    x1, x2, y1, y2 = add_margin(788, 805, 263, 278, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_click_edge_bank(android):
    x1, x2, y1, y2 = add_margin(172, 204, 526, 548, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_click_conveyor_belt(android):
    x1, x2, y1, y2 = add_margin(182, 225, 487, 516, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_conveyor_belt(android)


def OSRS_wait_click_conveyor_belt(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if not (add_color_margin(pix[876, 362], 190, 137, 6, 10)):
            sleep(randint(150, 350) / 1000)
            print("Conveyor belt clicked!")
            break


def OSRS_click__run_to_bar_dispenser(android):
    x1, x2, y1, y2 = add_margin(575, 589, 434, 450, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_click_bar_dispenser(android):
    x1, x2, y1, y2 = add_margin(529, 550, 368, 389, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_range(android)


def OSRS_click_bar_dispenser_2(android):
    x1, x2, y1, y2 = add_margin(594, 614, 429, 446, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(1600, 2000) / 1000)
    OSRS_wait_click_range(android)


def OSRS_wait_bars_smelted(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[71, 115], 44, 38, 31, 10):
            sleep(randint(150, 350) / 1000)
            print("Bars smelted!")
            break


def OSRS_wait_bars_smelted_2(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[162, 111], 44, 38, 31, 10):
            sleep(randint(150, 350) / 1000)
            print("Bars smelted!")
            break


def OSRS_wait_take_bars(android):
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[827, 357], 184, 133, 5, 10):
            sleep(randint(50, 150) / 1000)
            print("Bars taken!")
            break


def OSRS_blast_furnace_bank(android):
    x1, x2, y1, y2 = add_margin(673, 691, 227, 234, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_click_run_energy(android):
    x1, x2, y1, y2 = add_margin(783, 835, 146, 161, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)


def OSRS_drop_inventory(android):
    print("drop inventory test" + str(time.time()))
    number_list = list(range(1, 29))
    np.random.shuffle(number_list)

    for number in number_list:
        OSRS_click_item(android, number, 20, 120)
        sleep(randint(100, 150) / 1000)

    android.cooked_amount += 28
    android.amount_label.configure(text=str(int(android.amount_label.cget("text")) + 28))
    cooks_per_hour = " (" + str(
        int(android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) + " iron/h)"
    runtime = " (Runtime: " + str(int((int(time.time()) - int(android.start)) / 3600)) + "h " + str((int(
        (int(time.time()) - int(android.start)) / 60)) % 60) + "m " + str(
        (int(int(time.time()) - int(android.start))) % 60) + "s)"
    print("Resources " + android.name + ": " + str(android.cooked_amount) + cooks_per_hour + runtime)
    print("Xp/h: " + str(int((android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) * 35))


def OSRS_drop_inventory_barb_fishing(android):
    print("drop inventory test" + str(time.time()))
    number_list = list(range(3, 29))
    np.random.shuffle(number_list)

    for number in number_list:
        OSRS_click_item(android, number, 20, 120)
        sleep(randint(100, 150) / 1000)

    android.cooked_amount += 28
    android.amount_label.configure(text=str(int(android.amount_label.cget("text")) + 28))
    cooks_per_hour = " (" + str(
        int(android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) + " iron/h)"
    runtime = " (Runtime: " + str(int((int(time.time()) - int(android.start)) / 3600)) + "h " + str((int(
        (int(time.time()) - int(android.start)) / 60)) % 60) + "m " + str(
        (int(int(time.time()) - int(android.start))) % 60) + "s)"
    print("Resources " + android.name + ": " + str(android.cooked_amount) + cooks_per_hour + runtime)
    print("Xp/h: " + str(int((android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) * 35))


def OSRS_burn_inventory(android):
    number_list = list(range(3, 29))
    np.random.shuffle(number_list)

    last_pixel_count = count_pixels_improved(android)

    for number in number_list:
        if number % 2 == 0:
            OSRS_click_item(android, number, 20, 120)
            sleep(randint(100, 150) / 1000)
            OSRS_click_item(android, 2, 20, 120)
            sleep(randint(100, 150) / 1000)
        else:
            OSRS_click_item(android, 2, 20, 120)
            sleep(randint(100, 150) / 1000)
            OSRS_click_item(android, number, 20, 120)
            sleep(randint(100, 150) / 1000)

        last_pixel_count = OSRS_wait_xp_drop(android, last_pixel_count)
        sleep(randint(50, 200) / 1000)
    sleep(randint(250, 350) / 1000)


def OSRS_click_teleport_house_4(android):
    x1, x2, y1, y2 = add_margin(135, 155, 419, 441, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(350, 750) / 1000)
    android.input_press("KEYCODE_F1", 100, 250)
    OSRS_wait_click_teleport_house_4(android)
    sleep(randint(150, 250) / 1000)


def OSRS_wait_click_teleport_house_4(android):
    print(f"Waiting for teleport to Rellekka! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[515, 434], 70, 62, 61, 6):
            print(f"Teleported to Rellekka! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_click_firemaking_tile_1(android):
    x1, x2, y1, y2 = add_margin(581, 598, 389, 413, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_firemaking_tile_1(android)
    sleep(randint(150, 250) / 1000)


def OSRS_wait_click_firemaking_tile_1(android):
    print(f"Waiting for click firemaking tile 1! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[384, 430], 89, 81, 80, 6):
            print(f"Clicked firemaking tile 1! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_click_firemaking_tile_2(android):
    x1, x2, y1, y2 = add_margin(571, 588, 338, 349, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_click_firemaking_tile_2(android)
    sleep(randint(150, 250) / 1000)


def OSRS_wait_click_firemaking_tile_2(android):
    print(f"Waiting for click firemaking tile 2! {android.name}")
    while True:
        sleep(0.1)
        pix = android.screenshot()
        if add_color_margin(pix[377, 476], 87, 79, 78, 6):
            print(f"Clicked firemaking tile 2! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_click_amethyst_1_first(android):
    x1, x2, y1, y2 = add_margin(428, 558, 126, 191, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(350, 750) / 1000)


def OSRS_wait_amethyst_1_mined(android):
    print(f"Waiting for amethyst 1 mined! {android.name}")
    while True:
        sleep(1)
        pix = android.screenshot()

        if add_color_margin(pix[578, 49], 178, 163, 132, 10):
            print(f"Full inventory! {android.name}")
            OSRS_amethyst_clean_inventory(android)
            sleep(randint(50, 150) / 1000)
            break

        if add_color_margin(pix[816, 184], 68, 147, 49, 10):
            print(f"Speccing! {android.name}")
            x1, x2, y1, y2 = add_margin(811, 852, 177, 188, 3)
            clickX, clickY = randomized_click(x1, x2, y1, y2)
            android.input_tap(clickX, clickY)
            sleep(randint(50, 150) / 1000)

        if add_color_margin(pix[531, 240], 15, 13, 10, 10):
            print(f"Amethyst 1 mined! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_wait_amethyst_2_spawned(android):
    print(f"Waiting for amethyst 2 spawned! {android.name}")
    while True:
        sleep(1)
        pix = android.screenshot()
        if add_color_margin(pix[589, 240], 127, 72, 99, 10):
            print(f"Amethyst 2 spawned! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_click_amethyst_2(android):
    x1, x2, y1, y2 = add_margin(570, 702, 127, 182, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(350, 750) / 1000)


def OSRS_wait_amethyst_2_mined(android):
    print(f"Waiting for amethyst 2 mined! {android.name}")
    while True:
        sleep(1)
        pix = android.screenshot()

        if add_color_margin(pix[578, 49], 178, 163, 132, 10):
            print(f"Full inventory! {android.name}")
            OSRS_amethyst_clean_inventory(android)
            sleep(randint(50, 150) / 1000)
            break

        if add_color_margin(pix[816, 184], 68, 147, 49, 10):
            print(f"Speccing! {android.name}")
            x1, x2, y1, y2 = add_margin(811, 852, 177, 188, 3)
            clickX, clickY = randomized_click(x1, x2, y1, y2)
            android.input_tap(clickX, clickY)
            sleep(randint(50, 150) / 1000)

        if add_color_margin(pix[485, 238], 19, 15, 11, 10):
            print(f"Amethyst 2 mined! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_wait_amethyst_3_spawned(android):
    print(f"Waiting for amethyst 3 spawned! {android.name}")
    while True:
        sleep(1)
        pix = android.screenshot()
        if add_color_margin(pix[654, 245], 122, 70, 94, 10):
            print(f"Amethyst 3 spawned! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_click_amethyst_3(android):
    x1, x2, y1, y2 = add_margin(612, 719, 129, 173, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(350, 750) / 1000)


def OSRS_wait_amethyst_3_mined(android):
    print(f"Waiting for amethyst 3 mined! {android.name}")
    while True:
        sleep(1)
        pix = android.screenshot()

        if add_color_margin(pix[578, 49], 178, 163, 132, 10):
            print(f"Full inventory! {android.name}")
            OSRS_amethyst_clean_inventory(android)
            sleep(randint(50, 150) / 1000)
            break

        if add_color_margin(pix[816, 184], 68, 147, 49, 10):
            print(f"Speccing! {android.name}")
            x1, x2, y1, y2 = add_margin(811, 852, 177, 188, 3)
            clickX, clickY = randomized_click(x1, x2, y1, y2)
            android.input_tap(clickX, clickY)
            sleep(randint(50, 150) / 1000)

        if add_color_margin(pix[564, 240], 15, 13, 10, 10):
            print(f"Amethyst 3 mined! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_wait_amethyst_4_spawned(android):
    print(f"Waiting for amethyst 4 spawned! {android.name}")
    while True:
        sleep(1)
        pix = android.screenshot()
        if add_color_margin(pix[623, 238], 127, 72, 99, 10):
            print(f"Amethyst 4 spawned! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_click_amethyst_4(android):
    x1, x2, y1, y2 = add_margin(612, 720, 131, 170, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(350, 750) / 1000)


def OSRS_wait_amethyst_4_mined(android):
    print(f"Waiting for amethyst 4 mined! {android.name}")
    while True:
        sleep(1)
        pix = android.screenshot()

        if add_color_margin(pix[578, 49], 178, 163, 132, 10):
            print(f"Full inventory! {android.name}")
            OSRS_amethyst_clean_inventory(android)
            sleep(randint(50, 150) / 1000)
            break

        if add_color_margin(pix[816, 184], 68, 147, 49, 10):
            print(f"Speccing! {android.name}")
            x1, x2, y1, y2 = add_margin(811, 852, 177, 188, 3)
            clickX, clickY = randomized_click(x1, x2, y1, y2)
            android.input_tap(clickX, clickY)
            sleep(randint(50, 150) / 1000)

        if add_color_margin(pix[485, 237], 19, 15, 11, 10):
            print(f"Amethyst 4 mined! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_wait_amethyst_1_spawned(android):
    print(f"Waiting for amethyst 1 spawned! {android.name}")
    while True:
        sleep(1)
        pix = android.screenshot()
        print(pix[151,238])
        if add_color_margin(pix[151, 238], 84, 50, 67, 30):
            print(f"Amethyst 1 spawned! {android.name}")
            sleep(randint(50, 150) / 1000)
            break


def OSRS_click_amethyst_1(android):
    x1, x2, y1, y2 = add_margin(48, 139, 132, 171, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(350, 750) / 1000)


def OSRS_amethyst_clean_inventory(android):
    indexes = []

    pix = android.screenshot()

    found_amethyst_index = False
    amethyst_index = 0

    if not(add_color_margin(pix[928, 367], 156, 83, 121, 15)):
        indexes.append(4)
    else:
        if not found_amethyst_index:
            amethyst_index = 4
            found_amethyst_index = True

    if not(add_color_margin(pix[785, 408], 156, 83, 121, 15)):
        indexes.append(5)
    else:
        if not found_amethyst_index:
            amethyst_index = 5
            found_amethyst_index = True

    if not(add_color_margin(pix[832, 408], 156, 83, 121, 15)):
        indexes.append(6)
    else:
        if not found_amethyst_index:
            amethyst_index = 6
            found_amethyst_index = True

    if not(add_color_margin(pix[880, 408], 156, 83, 121, 15)):
        indexes.append(7)
    else:
        if not found_amethyst_index:
            amethyst_index = 8
            found_amethyst_index = True

    if not(add_color_margin(pix[928, 408], 156, 83, 121, 15)):
        indexes.append(8)
    else:
        if not found_amethyst_index:
            amethyst_index = 8
            found_amethyst_index = True

    if not(add_color_margin(pix[785, 448], 156, 83, 121, 15)):
        indexes.append(9)
    else:
        if not found_amethyst_index:
            amethyst_index = 9
            found_amethyst_index = True

    if not(add_color_margin(pix[832, 448], 156, 83, 121, 15)):
        indexes.append(10)
    else:
        if not found_amethyst_index:
            amethyst_index = 10
            found_amethyst_index = True

    if not(add_color_margin(pix[880, 448], 156, 83, 121, 15)):
        indexes.append(11)
    else:
        if not found_amethyst_index:
            amethyst_index = 11
            found_amethyst_index = True

    if not(add_color_margin(pix[928, 448], 156, 83, 121, 15)):
        indexes.append(12)
    else:
        if not found_amethyst_index:
            amethyst_index = 12
            found_amethyst_index = True

    if not(add_color_margin(pix[785, 491], 156, 83, 121, 15)):
        indexes.append(13)
    else:
        if not found_amethyst_index:
            amethyst_index = 13
            found_amethyst_index = True

    if not(add_color_margin(pix[832, 491], 156, 83, 121, 15)):
        indexes.append(14)
    else:
        if not found_amethyst_index:
            amethyst_index = 14
            found_amethyst_index = True

    if not(add_color_margin(pix[880, 491], 156, 83, 121, 15)):
        indexes.append(15)
    else:
        if not found_amethyst_index:
            amethyst_index = 15
            found_amethyst_index = True

    if not(add_color_margin(pix[928, 491], 156, 83, 121, 15)):
        indexes.append(16)
    else:
        if not found_amethyst_index:
            amethyst_index = 16
            found_amethyst_index = True

    if not(add_color_margin(pix[785, 531], 156, 83, 121, 15)):
        indexes.append(17)
    else:
        if not found_amethyst_index:
            amethyst_index = 17
            found_amethyst_index = True

    if not(add_color_margin(pix[832, 531], 156, 83, 121, 15)):
        indexes.append(18)
    else:
        if not found_amethyst_index:
            amethyst_index = 18
            found_amethyst_index = True

    if not(add_color_margin(pix[880, 531], 156, 83, 121, 15)):
        indexes.append(19)
    else:
        if not found_amethyst_index:
            amethyst_index = 19
            found_amethyst_index = True

    if not(add_color_margin(pix[928, 531], 156, 83, 121, 15)):
        indexes.append(20)
    else:
        if not found_amethyst_index:
            amethyst_index = 20
            found_amethyst_index = True

    if not(add_color_margin(pix[785, 572], 156, 83, 121, 15)):
        indexes.append(21)
    else:
        if not found_amethyst_index:
            amethyst_index = 21
            found_amethyst_index = True

    if not(add_color_margin(pix[832, 572], 156, 83, 121, 15)):
        indexes.append(22)
    else:
        if not found_amethyst_index:
            amethyst_index = 22
            found_amethyst_index = True

    if not(add_color_margin(pix[880, 572], 156, 83, 121, 15)):
        indexes.append(23)
    else:
        if not found_amethyst_index:
            amethyst_index = 23
            found_amethyst_index = True

    if not(add_color_margin(pix[928, 572], 156, 83, 121, 15)):
        indexes.append(24)
    else:
        if not found_amethyst_index:
            amethyst_index = 24
            found_amethyst_index = True

    if not(add_color_margin(pix[785, 614], 156, 83, 121, 15)):
        indexes.append(25)
    else:
        if not found_amethyst_index:
            amethyst_index = 25
            found_amethyst_index = True

    if not(add_color_margin(pix[832, 614], 156, 83, 121, 15)):
        indexes.append(26)
    else:
        if not found_amethyst_index:
            amethyst_index = 26
            found_amethyst_index = True

    if not(add_color_margin(pix[880, 614], 156, 83, 121, 15)):
        indexes.append(27)
    else:
        if not found_amethyst_index:
            amethyst_index = 27
            found_amethyst_index = True

    if not(add_color_margin(pix[928, 614], 156, 83, 121, 15)):
        indexes.append(28)
    else:
        if not found_amethyst_index:
            amethyst_index = 28
            found_amethyst_index = True

    OSRS_click_item(android, 1, 50, 150)
    OSRS_click_item(android, amethyst_index, 50, 150)

    while True:
        sleep(1)
        pix = android.screenshot()
        if add_color_margin(pix[358, 29], 204, 186, 149, 10):
            print(f"Popup opened! {android.name}")
            sleep(randint(50, 150) / 1000)
            break

    android.input_press("KEYCODE_4", 0, 0)
    sleep(30)

    if not (len(indexes) == 0):
        OSRS_toggle_mode(android, 50, 150, True)
        for index in indexes:
            OSRS_click_item(android, index, 50, 150)
        OSRS_toggle_mode(android, 50, 150, False)
