from osrs.steps import *

from pyautogui import *
from pynput.keyboard import Listener, Controller, Key


def OSRS_agility_seers(android):
    while True:
        tries = 0
        last_pixel_count = count_pixels(android)
        OSRS_agility_seers_obstacle_1(android)
        last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
        sleep(randint(300, 500) / 1000)

        if last_pixel_count != 0:
            break
        print("Failed, teleporting back to seers!")
        OSRS_click_teleport_seers(android)
        sleep(randint(4000, 6000) / 1000)
        tries += 1
        if tries > 5:
            sys.exit(0)

    OSRS_agility_seers_obstacle_2(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    if last_pixel_count == 0:
        OSRS_click_teleport_seers(android)
        sleep(randint(4000, 6000) / 1000)
        return
    sleep(randint(50, 250) / 1000)

    OSRS_agility_seers_obstacle_3(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    if last_pixel_count == 0:
        OSRS_click_teleport_seers(android)
        sleep(randint(4000, 6000) / 1000)
        return
    sleep(randint(800, 1000) / 1000)

    OSRS_agility_seers_obstacle_4(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    if last_pixel_count == 0:
        OSRS_click_teleport_seers(android)
        sleep(randint(4000, 6000) / 1000)
        return
    sleep(randint(150, 300) / 1000)

    OSRS_agility_seers_obstacle_5(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    if last_pixel_count == 0:
        OSRS_click_teleport_seers(android)
        sleep(randint(4000, 6000) / 1000)
        return
    sleep(randint(50, 250) / 1000)

    OSRS_agility_seers_obstacle_6(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    if last_pixel_count == 0:
        OSRS_click_teleport_seers(android)
        sleep(randint(4000, 6000) / 1000)
        return
    sleep(randint(100, 300) / 1000)
    OSRS_click_teleport_seers(android)


def OSRS_agility_falador(android):
    last_pixel_count = count_pixels_2(android)
    OSRS_agility_falador_obstacle_1(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_2(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(1200, 1400) / 1000)

    OSRS_agility_falador_obstacle_3(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_4(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_5(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_6(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(800, 1000) / 1000)

    OSRS_agility_falador_obstacle_7(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_8(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_9(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_10(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_11(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_12(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(600, 800) / 1000)

    OSRS_agility_falador_obstacle_13(android)
    last_pixel_count = OSRS_wait_obstacle_done_3(android, last_pixel_count)
    sleep(randint(800, 1000) / 1000)


def OSRS_agility_ardy(android):
    # if boost needed for 96 agility
    # if android.lap_number % 5 == 0:
    #     if android.lap_number % 10 == 0 and android.lap_number != 0:
    #         android.pie_number += 1
    #         OSRS_click_item(android, android.pie_number, 150, 250)
    #     else:
    #         OSRS_click_item(android, android.pie_number, 150, 250)

    last_pixel_count = count_pixels(android)
    OSRS_agility_ardy_obstacle_1(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    sleep(randint(50, 200) / 1000)

    OSRS_agility_ardy_obstacle_2(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    sleep(randint(50, 200) / 1000)

    OSRS_agility_ardy_obstacle_3(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    sleep(randint(50, 200) / 1000)

    if android.pickup:
        OSRS_agility_ardy_pick_up_marks(android)
        sleep(randint(1500, 3000) / 1000)

    OSRS_agility_ardy_obstacle_4(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    sleep(randint(50, 200) / 1000)

    OSRS_agility_ardy_obstacle_5(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    sleep(randint(50, 200) / 1000)

    OSRS_agility_ardy_obstacle_6(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    sleep(randint(50, 200) / 1000)

    OSRS_agility_ardy_obstacle_7(android)
    last_pixel_count = OSRS_wait_obstacle_done_2(android, last_pixel_count)
    sleep(randint(50, 200) / 1000)

    # if boost needed for 96 agility
    # android.lap_number += 1


def OSRS_bank_myths(android):
    OSRS_click_myths_bank(android)
    OSRS_wait_bank_open(android)
    android.status_label["text"] = "Banking"
    android.status = "Banking"
    sleep(randint(150, 350) / 1000)
    OSRS_deposit_item(android, 50, 150)
    OSRS_withdraw_item(android, 50, 150)
    android.input_press("KEYCODE_ESCAPE", 150, 350)


def OSRS_bank_myths_firemaking(android):
    OSRS_click_myths_bank(android)
    OSRS_wait_bank_open(android)
    android.status_label["text"] = "Banking"
    android.status = "Banking"
    sleep(randint(150, 350) / 1000)
    OSRS_withdraw_item(android, 50, 150)
    android.input_press("KEYCODE_ESCAPE", 150, 350)


def OSRS_cook_myths(android):
    OSRS_click_myths_range(android)
    OSRS_wait_click_range(android)
    android.status_label["text"] = "Cooking"
    android.status = "Cooking"
    sleep(randint(150, 350) / 1000)
    android.input_press("KEYCODE_SPACE", 0, 0)
    OSRS_wait_started_cooking(android)
    sleep(randint(65000, 66000) / 1000)


def OSRS_fletch_bows_myths(android):
    OSRS_click_myths_bank(android)
    OSRS_wait_bank_open(android)
    android.status_label["text"] = "Banking"
    android.status = "Banking"

    sleep(randint(150, 250) / 1000)
    OSRS_deposit_item(android, 85, 120)
    OSRS_withdraw_item_1(android, 85, 120)
    OSRS_withdraw_item_2(android, 85, 120)
    android.input_press("KEYCODE_ESCAPE", 150, 250)

    OSRS_click_item(android, 13, 120, 150)
    OSRS_click_item(android, 17, 70, 90)
    OSRS_wait_click_range(android)
    android.status_label["text"] = "Cooking"
    android.status = "Cooking"
    sleep(randint(50, 120) / 1000)
    android.input_press("KEYCODE_1", 0, 0)
    sleep(randint(16450, 16750) / 1000)


def OSRS_make_staminas_myths(android):
    OSRS_click_myths_bank(android)
    OSRS_wait_bank_open(android)
    android.status_label["text"] = "Banking"
    android.status = "Banking"

    sleep(randint(150, 250) / 1000)
    OSRS_deposit_item(android, 85, 120)
    OSRS_withdraw_item_1(android, 85, 120)
    android.input_press("KEYCODE_ESCAPE", 200, 250)
    OSRS_click_item(android, 28, 120, 150)
    OSRS_click_item(android, 27, 70, 90)
    OSRS_wait_click_range(android)
    android.status_label["text"] = "Cooking"
    android.status = "Cooking"
    sleep(randint(150, 250) / 1000)
    android.input_press("KEYCODE_1", 0, 0)
    sleep(randint(31600, 32000) / 1000)


def OSRS_barb_fishing(android):
    pix = android.screenshot()
    find_square(pix, android)
    sleep(10)
    while True:
        sleep(0.1)
        pix = android.screenshot()

        if not (pix[532, 22] == (0, 0, 0)):
            print(f"Interface open! {android.name}")
            OSRS_drop_inventory_barb_fishing(android)
            break

        # if not (add_color_margin(pix[501, 388], 18, 22, 7, 10)):
        #     print(f"Not at fishing spot! {android.name}")
        #     pix = android.screenshot()
        #     find_square(pix, android)
        #     sleep(10)

        fishing1 = False
        fishing2 = False
        for y in range(390, 460):
            if pix[515, y] == (21, 253, 255):
                fishing1 = True

        for x in range(460, 505):
            if pix[x, 386] == (21, 253, 255):
                fishing2 = True

        if not fishing1 and not fishing2:
            print(f"Not at fishing spot! {android.name}")
            pix = android.screenshot()
            find_square(pix, android)
            sleep(10)


def OSRS_bank_guild(android):
    if android.status == "Cooking":
        OSRS_click_guild_bank(android)
    else:
        OSRS_click_guild_bank_first(android)
    OSRS_wait_bank_open(android)
    android.status_label["text"] = "Banking"
    android.status = "Banking"
    sleep(randint(150, 350) / 1000)
    OSRS_deposit_item(android, 50, 150)
    OSRS_withdraw_item(android, 50, 150)
    android.input_press("KEYCODE_ESCAPE", 150, 350)


def OSRS_cook_guild(android):
    OSRS_click_guild_range(android)
    OSRS_wait_click_range(android)
    android.status_label["text"] = "Cooking"
    android.status = "Cooking"
    sleep(randint(150, 350) / 1000)
    android.input_press("KEYCODE_1", 0, 0)
    OSRS_wait_started_cooking(android)
    sleep(randint(65000, 66000) / 1000)


def OSRS_bank_varrock(android):
    OSRS_click_varrock_bank(android)
    OSRS_wait_bank_open(android)
    android.status_label["text"] = "Banking"
    android.status = "Banking"
    sleep(randint(300, 800) / 1000)
    OSRS_deposit_item(android, 300, 800)
    OSRS_withdraw_item_1(android, 300, 800)
    OSRS_withdraw_item_2(android, 300, 800)
    android.input_press("KEYCODE_ESCAPE", 100, 500)


def OSRS_make_wine(android):
    OSRS_click_item_17(android, 300, 800)
    OSRS_click_item_13(android)
    OSRS_wait_click_range(android)
    android.status_label["text"] = "Cooking"
    android.status = "Cooking"
    sleep(randint(200, 600) / 1000)
    android.input_press("KEYCODE_1", 0, 0)


def OSRS_fish_karambwans(android):
    android.status_label["text"] = "Fishing"
    android.status = "Fishing"
    android.input_press("KEYCODE_F3", 800, 1500)
    OSRS_click_teleport_house(android)
    OSRS_wait_click_teleport_house(android)
    OSRS_toggle_mode(android, 300, 800, True)
    clickX, clickY = OSRS_click_poh_fairy_ring(android)
    OSRS_click_last_destination(android, clickX, clickY)
    OSRS_toggle_mode(android, 300, 800, False)
    OSRS_click_fishing_spot(android)


def OSRS_bank_karambwans(android):
    OSRS_wait_interface_open(android)
    android.status_label["text"] = "Banking"
    android.status = "Banking"
    OSRS_close_interface(android)
    android.input_press("KEYCODE_F4", 800, 1500)
    OSRS_toggle_mode(android, 300, 800, True)
    clickX, clickY = OSRS_click_crafting_cape(android)
    OSRS_teleport_crafting_guild(android, clickX, clickY)
    OSRS_toggle_mode(android, 300, 800, False)
    OSRS_click_crafting_guild_bank(android)
    OSRS_wait_bank_open(android)
    sleep(randint(300, 800) / 1000)
    OSRS_deposit_item(android, 300, 800)
    android.input_press("KEYCODE_ESCAPE", 300, 800)


def OSRS_make_planks(android):
    OSRS_toggle_mode(android, 50, 150, True)
    clickX, clickY = OSRS_click_crafting_cape(android)
    OSRS_teleport_crafting_guild_2(android, clickX, clickY)
    OSRS_toggle_mode(android, 50, 150, False)
    OSRS_click_crafting_guild_bank(android)
    OSRS_wait_bank_open(android)
    OSRS_withdraw_item_1(android, 100, 200)
    android.input_press("KEYCODE_ESCAPE", 100, 200)

    OSRS_click_teleport_house_3(android)
    OSRS_click_house_options(android)
    OSRS_click_call_servant(android)
    android.input_press("KEYCODE_1", 0, 0)
    OSRS_wait_next_dialog(android, True)
    android.input_press("KEYCODE_SPACE", 0, 0)
    OSRS_wait_next_dialog(android, False)
    android.input_press("KEYCODE_1", 0, 0)
    OSRS_wait_next_dialog(android, True)
    android.input_press("KEYCODE_SPACE", 0, 0)
    sleep(randint(50, 150) / 1000)
    android.input_press("KEYCODE_F4", 50, 150)
    OSRS_wait_interface_close(android)


def OSRS_make_myth_rack(android):
    count = 0
    OSRS_click_house_options(android)
    OSRS_wait_click_house_options(android)
    OSRS_click_call_servant(android)
    OSRS_wait_call_servant(android)
    android.input_press("KEYCODE_1", 0, 0)
    OSRS_wait_interface_close_2(android)

    clickX, clickY = OSRS_make_myth_rack_1(android)
    OSRS_make_myth_rack_2(android, clickX, clickY)
    android.input_press("KEYCODE_4", 0, 0)
    OSRS_wait_construction_popup_close(android)
    sleep(randint(450, 500) / 1000)
    clickX, clickY = OSRS_make_myth_rack_1(android)
    OSRS_make_myth_rack_5(android, clickX, clickY)
    OSRS_wait_interface_open_2(android)
    android.input_press("KEYCODE_1", 0, 0)
    OSRS_wait_interface_close_2(android)

    OSRS_wait_interface_open_2(android)

    while True:
        clickX, clickY = OSRS_make_myth_rack_1(android)
        OSRS_make_myth_rack_2(android, clickX, clickY)
        android.input_press("KEYCODE_4", 0, 0)
        OSRS_wait_construction_popup_close(android)
        sleep(randint(550, 600) / 1000)
        clickX, clickY = OSRS_make_myth_rack_1(android)
        OSRS_make_myth_rack_5(android, clickX, clickY)
        OSRS_wait_interface_open_2(android)
        android.input_press("KEYCODE_1", 0, 0)
        OSRS_wait_interface_close_2(android)
        count += 1
        if count == 7:
            break


def OSRS_chop_teaks(android):
    android.input_press("KEYCODE_F3", 200, 550)
    OSRS_click_teleport_house_2(android)
    OSRS_click_poh_pendant(android)
    OSRS_wait_click_poh_pendant(android)
    OSRS_toggle_mode(android, 50, 300, True)
    if OSRS_find_barge_guard(android):
        OSRS_toggle_mode(android, 150, 300, False)
        android.input_press("KEYCODE_F1", 200, 550)
        OSRS_chop_teaks_bank(android)
        return
    OSRS_toggle_mode(android, 150, 300, False)
    OSRS_click_hole(android)
    android.input_press("KEYCODE_F1", 200, 550)

    OSRS_click_tree_1(android)
    if OSRS_wait_click_tree_1_chopped(android):
        OSRS_chop_teaks_bank(android)
        return

    OSRS_click_tree_2(android)
    if OSRS_wait_click_tree_2_chopped(android):
        OSRS_chop_teaks_bank(android)
        return
    while True:
        OSRS_wait_tree_1_2_respawned(android)
        OSRS_click_tree_1_2(android)
        if OSRS_wait_click_tree_1_2_chopped(android):
            OSRS_chop_teaks_bank(android)
            return

        OSRS_wait_tree_2_1_respawned(android)
        OSRS_click_tree_2_1(android)
        if OSRS_wait_click_tree_2_chopped(android):
            OSRS_chop_teaks_bank(android)
            return


def OSRS_chop_teaks_2(android):
    OSRS_wait_tree_1_2_respawned(android)
    OSRS_click_tree_1_2(android)
    if OSRS_wait_click_tree_1_2_chopped(android):
        OSRS_drop_inventory(android)

    OSRS_wait_tree_2_1_respawned(android)
    OSRS_click_tree_2_1(android)
    if OSRS_wait_click_tree_2_chopped(android):
        OSRS_drop_inventory(android)


# TODO
# Make screenshotting a different thread running 24/7 updating global variables like: ore 1 respawned etc.
# This way you don't have to check if next ore to click is respawned
def OSRS_mine_iron(android):
    OSRS_wait_iron_ore_1_respawned(android)
    OSRS_click_iron_ore_1(android)

    OSRS_wait_iron_ore_2_respawned(android)
    OSRS_click_iron_ore_2(android)

    OSRS_wait_iron_ore_3_respawned(android)
    OSRS_click_iron_ore_3(android)


def OSRS_mine_iron_2(android):
    pix = android.screenshot()

    if add_color_margin(pix[924, 609], 39, 17, 11, 10):
        print(f"Inventory full! {android.name}")
        sleep(randint(20, 100) / 1000)
        OSRS_drop_inventory(android)

    # Ore 1
    x1, x2, y1, y2 = add_margin(397, 593, 641, 741, 25)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(2085, 2105) / 1000)

    # Ore 2
    x1, x2, y1, y2 = add_margin(171, 270, 443, 600, 25)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(2085, 2105) / 1000)

    # Ore 3
    x1, x2, y1, y2 = add_margin(652, 731, 491, 620, 25)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    sleep(randint(2085, 2105) / 1000)
    OSRS_click_item(android, 1, 25, 30)
    OSRS_click_item(android, 2, 25, 30)
    OSRS_click_item(android, 3, 25, 30)
    android.cooked_amount += 3


def OSRS_chop_teaks_bank(android):
    android.input_press("KEYCODE_SPACE", 0, 0)
    OSRS_wait_interface_close(android)
    android.input_press("KEYCODE_F4", 200, 550)
    OSRS_toggle_mode(android, 150, 300, True)
    clickX, clickY = OSRS_click_crafting_cape(android)
    OSRS_teleport_crafting_guild_north(android, clickX, clickY)
    OSRS_toggle_mode(android, 150, 300, False)
    OSRS_click_crafting_guild_bank_north(android)
    OSRS_wait_bank_open(android)
    OSRS_deposit_item(android, 150, 350)
    android.input_press("KEYCODE_ESCAPE", 100, 500)


def OSRS_fletch_myths(android):
    OSRS_click_myths_bank(android)
    OSRS_wait_bank_open(android)
    android.status_label["text"] = "Banking"
    android.status = "Banking"
    sleep(randint(150, 350) / 1000)
    OSRS_withdraw_item(android, 50, 150)
    android.input_press("KEYCODE_ESCAPE", 150, 350)

    OSRS_click_item_1(android)
    OSRS_click_item_5(android)
    OSRS_wait_interface_open_2(android)
    sleep(randint(150, 350) / 1000)
    android.input_press("KEYCODE_1", 0, 0)
    OSRS_wait_interface_close_2(android)
    OSRS_wait_fletching_done_myths(android)


def OSRS_make_arrows(android):
    OSRS_click_item_1(android)
    OSRS_click_item_5(android)
    OSRS_wait_interface_open_2(android)
    android.input_press("KEYCODE_1", 0, 0)
    OSRS_wait_interface_close_2(android)
    sleep(randint(10200, 10550) / 1000)


def OSRS_redwood_fletch_make_arrows(android):
    OSRS_click_redwood_tree(android)

    while True:
        OSRS_make_arrows(android)
        if OSRS_check_redwood_tree_respawned(android):
            break

    if OSRS_check_redwood_inventory_full(android):
        OSRS_click_item_2(android)
        OSRS_click_item_6(android)
        OSRS_wait_interface_open_2(android)
        sleep(randint(150, 350) / 1000)
        android.input_press("KEYCODE_1", 0, 0)
        OSRS_wait_redwood_inventory_done(android)


def OSRS_bank_edge(android):
    OSRS_click_edge_bank(android)
    OSRS_wait_bank_open(android)
    android.status_label["text"] = "Banking"
    android.status = "Banking"
    sleep(randint(150, 350) / 1000)
    OSRS_deposit_item(android, 50, 150)
    OSRS_withdraw_item(android, 50, 150)
    #android.input_press("KEYCODE_ESCAPE", 150, 350)


def OSRS_smith_edge(android):
    OSRS_click_edge_furnace(android)
    OSRS_wait_click_range(android)
    android.status_label["text"] = "Cooking"
    android.status = "Cooking"
    sleep(randint(150, 350) / 1000)
    android.input_press("KEYCODE_1", 0, 0)
    OSRS_wait_started_cooking(android)
    sleep(randint(156000, 159000) / 1000)


def OSRS_smith_blast_furnace(android):
    OSRS_click_item(android, 1, 50, 100)
    OSRS_click_conveyor_belt(android)
    OSRS_click__run_to_bar_dispenser(android)
    OSRS_wait_bars_smelted(android)
    OSRS_click_item(android, 1, 50, 100)
    sleep(randint(1000, 1050) / 1000)
    OSRS_click_bar_dispenser(android)
    android.input_press("KEYCODE_1", 40, 75)
    #OSRS_wait_take_bars(android)

    OSRS_blast_furnace_bank(android)
    OSRS_wait_bank_open(android)
    sleep(randint(150, 350) / 1000)
    OSRS_deposit_item(android, 50, 150)

    pix = android.screenshot()
    if not (add_color_margin(pix[705, 697], 120, 79, 34, 10)):
        OSRS_click_quantity_1(android, 50, 150)
        OSRS_withdraw_item_2(android, 50, 150)
        OSRS_click_quantity_all(android, 50, 150)
        OSRS_withdraw_item(android, 50, 150)
        android.input_press("KEYCODE_ESCAPE", 200, 250)
        OSRS_click_item(android, 2, 50, 100)

    else:
        OSRS_withdraw_item(android, 50, 150)
        android.input_press("KEYCODE_ESCAPE", 150, 350)


def OSRS_smith_blast_furnace_2(android):
    pix = android.screenshot()
    if add_color_margin(pix[789, 152], 0, 59, 1, 10):
        OSRS_click_run_energy(android)
        sleep(randint(150, 350) / 1000)

    OSRS_click_item(android, 1, 50, 100)
    OSRS_click_conveyor_belt(android)
    OSRS_wait_bars_smelted(android)
    OSRS_click_item(android, 1, 50, 100)
    sleep(randint(1000, 1200) / 1000)
    OSRS_click_bar_dispenser(android)
    android.input_press("KEYCODE_1", 0, 0)
    OSRS_wait_take_bars(android)

    OSRS_blast_furnace_bank(android)
    OSRS_wait_bank_open(android)
    sleep(randint(150, 350) / 1000)
    OSRS_deposit_item(android, 50, 150)
    OSRS_withdraw_item(android, 50, 150)
    android.input_press("KEYCODE_ESCAPE", 150, 350)


def OSRS_burn_logs_semi(android):
    tile_1 = True

    while True:
        android.input_press("KEYCODE_F4", 300, 550)
        OSRS_toggle_mode(android, 150, 300, True)
        clickX, clickY = OSRS_click_crafting_cape(android)
        OSRS_teleport_crafting_guild_north(android, clickX, clickY)
        OSRS_toggle_mode(android, 150, 300, False)
        OSRS_click_crafting_guild_bank_north(android)
        OSRS_wait_bank_open(android)
        OSRS_withdraw_item_1(android, 100, 300)
        android.input_press("KEYCODE_ESCAPE", 100, 250)
        android.input_press("KEYCODE_F3", 100, 250)
        OSRS_click_teleport_house_4(android)

        if tile_1:
            OSRS_click_firemaking_tile_1(android)
        else:
            OSRS_click_firemaking_tile_2(android)

        tile_1 = not tile_1
        OSRS_burn_inventory(android)

        android.cooked_amount += 26
        android.amount_label.configure(text=str(int(android.amount_label.cget("text")) + 26))
        cooks_per_hour = " (" + str(
            int(android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) + " cooks/h)"
        runtime = " (Runtime: " + str(int((int(time.time()) - int(android.start)) / 3600)) + "h " + str((int(
            (int(time.time()) - int(android.start)) / 60)) % 60) + "m " + str(
            (int(int(time.time()) - int(android.start))) % 60) + "s)"
        print("Resources " + android.name + ": " + str(android.cooked_amount) + cooks_per_hour + runtime)
        print("Xp/h: " + str(int((android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) * 353))


def input_thread_firemaking(android):
    # Handling on keypress and on keyrelease event
    def on_press(key):
        print("Key pressed: " + str(key))

        if str(key) == "Key.ctrl_r":
            android.firemake = True

    def on_release(key):
        pass

    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()


def OSRS_mine_amethyst(android):
    # Zoom out 5 times

    while True:
        OSRS_wait_amethyst_1_spawned(android)
        OSRS_click_amethyst_1(android)
        sleep(5)
        OSRS_wait_amethyst_1_mined(android)

        OSRS_wait_amethyst_2_spawned(android)
        OSRS_click_amethyst_2(android)
        sleep(5)
        OSRS_wait_amethyst_2_mined(android)

        OSRS_wait_amethyst_3_spawned(android)
        OSRS_click_amethyst_3(android)
        sleep(5)
        OSRS_wait_amethyst_3_mined(android)

        OSRS_wait_amethyst_4_spawned(android)
        OSRS_click_amethyst_4(android)
        sleep(5)
        OSRS_wait_amethyst_4_mined(android)





def OSRS_wait_started_cooking(android):
    print(f"Waiting for started cooking! {android.name}")
    start = time.time()
    while True:
        sleep(0.1)

        if android.script_stopped:
            android.status_label["text"] = "Stopped"
            exit(0)

        if (time.time() - start) > 80:
            android.cooking_fails += 1
            if android.cooking_fails == 2:
                android.stop_script()
                break
            break

        pix = android.screenshot()
        if pix[532, 22] == (0, 0, 0):
            print(f"Cooking started! {android.name}")
            if android.script_stopped:
                android.status_label["text"] = "Stopped"
                exit(0)
            android.cooking_fails = 0
            break


def OSRS_login(android, t1, t2, manual):
    # Step 1
    android.status_label["text"] = "Login"
    x1, x2, y1, y2 = add_margin(397, 625, 275, 332, 10)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_login_1(android, manual)
    sleep(randint(800, 1500) / 1000)

    # Step 2
    x1, x2, y1, y2 = add_margin(394, 629, 348, 426, 10)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_login_2(android, manual)
    sleep(randint(t1, t2) / 1000)


def OSRS_logout(android, t1, t2, manual):
    android.timer_stop = True
    android.input_press("KEYCODE_ESCAPE", 300, 800)
    x1, x2, y1, y2 = add_margin(777, 925, 584, 608, 3)
    clickX, clickY = randomized_click(x1, x2, y1, y2)
    android.input_tap(clickX, clickY)
    OSRS_wait_logout(android, manual)
    android.status_label["text"] = "Logout"
    if not manual:
        sleep_with_checks(android, randint(t1, t2) / 1000)


def OSRS_test(android):
    android.input_tap(183, 517)
    sleep(5)
    android.input_tap(183, 517)