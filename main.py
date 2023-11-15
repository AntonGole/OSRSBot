import Util.calibration as calibrations

from Application.script import *

from Application.app import App

from Application.android import Android

from PIL import Image, ImageTk

cook_myths = [
        [OSRS_bank_myths],
        [OSRS_cook_myths],
        [update_info, 28]
        ]

cook_guild = [
            [OSRS_bank_guild],
            [OSRS_cook_guild],
            [OSRS_wait_started_cooking],
            [update_info, 28]
        ]


smith_edge = [
            [OSRS_smith_edge],
            [OSRS_bank_edge],
            [update_info, 27]
        ]

make_wine = [
            [OSRS_bank_varrock],
            [OSRS_make_wine],
            [OSRS_wait_started_cooking],
            [wait, 17000, 17600],
            [update_info, 14]
        ]


fletch_bows_myths = [
            [OSRS_fletch_bows_myths],
            [update_info, 14]
        ]

cook_karambwans = [
            [OSRS_fish_karambwans],
            [OSRS_bank_karambwans],
            [update_info, 28]
        ]

agility_falador = [
            [OSRS_agility_falador],
            [update_info, 1]
        ]


agility_seers = [
            [OSRS_agility_seers],
            [update_info, 1]
        ]


agility_ardy = [
            [OSRS_agility_ardy],
            [update_info, 1]
        ]


make_planks = [
            [OSRS_make_planks],
            [update_info, 26]
        ]


make_myth_rack = [
            [OSRS_make_myth_rack],
            [update_info, 24]
        ]


chop_teaks = [
            [OSRS_chop_teaks],
            [update_info, 27]
        ]


fletch_myths = [
            [OSRS_fletch_myths],
            [update_info, 26]
        ]


make_arrows = [
            [OSRS_make_arrows],
            [update_info, 150]
        ]


redwood_fletch_make_arrows = [
            [OSRS_redwood_fletch_make_arrows],
            [update_info, 150]
        ]


chop_teaks_2 = [
            [OSRS_chop_teaks_2]
        ]

mine_iron = [
            [OSRS_mine_iron]
        ]


mine_iron_2 = [
            [OSRS_mine_iron_2]
        ]


blast_furnace_gold = [
            [OSRS_smith_blast_furnace],
            [update_info, 27]
        ]


staminas_myths = [
            [OSRS_make_staminas_myths],
            [update_info, 27]
        ]


barb_fishing = [
            [OSRS_barb_fishing],
            [update_info, 26]
        ]


firemake_semi = [
            [OSRS_burn_logs_semi],
        ]


mine_amethyst = [
            [OSRS_mine_amethyst]
        ]

test_script = [
    [OSRS_test]
]


def instantiate_androids():
    #android4 = Android("Android 4", "192.168.0.246:5555", "192.168.0.246", 7150, agility_seers, 4)
    #android4 = Android("Android 4", "192.168.0.248:5555", "192.168.0.248", 10000, mine_iron_2, 4)
    #android4 = Android("Android 4", "192.168.0.246:5555", "192.168.0.246", 50000, cook_myths, 1)
    android4 = Android("Android 4", "192.168.0.246:5555", "192.168.0.246", 10000, test_script, 4)


    #android5 = Android("Android 5", "192.168.0.48:5555", "192.168.0.48", 50000, smith_edge, 10)
    #android6 = Android("Android 6", "192.168.0.49:5555", "192.168.0.49", 50000, smith_edge, 10)
    #android8 = Android("Android 8", "192.168.0.186:5555", "192.168.0.186", 50000, smith_edge, 10)
    #android5 = Android("Android 5", "192.168.0.49:5555", "192.168.0.49", 50000, cook_guild, 2)
    #android6 = Android("Android 6", "192.168.0.48:5555", "192.168.0.48", 50000, cook_guild, 2)
    #android7 = Android("Android 7", "192.168.0.173:5555", "192.168.0.173", 50000, cook_guild, 2)
    #android8 = Android("Android 8", "192.168.0.186:5555", "192.168.0.186", 50000, cook_guild, 2)
    #android9 = Android("Android 9", "192.168.0.109:5555", "192.168.0.109", 50000, cook_guild, 2)

    # return [android1, android2, android3, android4, android5, android6]
    #return [android3, android4, android6, android7]
    #return [android4, android5, android6, android7]
    #return [android4, android5, android6, android9]
    #return [android4, android6, android7]
    #return [android5, android6, android7, android8]
    return [android4]


def connect_androids():
    count_cooked()
    androids = instantiate_androids()
    cmd("adb disconnect")
    sleep(3)
    cmd("adb kill-server")
    sleep(3)

    for android in androids:
        android.connect()


def main():
    androids = instantiate_androids()
    connect_androids()
    app = App(androids)
    app.run()


def calibrate_coordinates():
    title_name = "Android 4 [Running] - Oracle VM VirtualBox"
    coordinateString = []
    thread = threading.Thread(target=lambda: calibrations.input_thread(
        coordinateString, title_name), args=(), daemon=True)
    thread.start()
    calibrations.print_coordinates(title_name)
    calibrations.sleep(5000)


def count_cooked():
    total_amount = 0
    for i in range(1):
        with open(f"logs/3.txt", "r") as file:
            logged_amount = file.readline()
            total_amount += int(logged_amount)
    with open(f"logs/total.txt", "w") as file:
        file.seek(0)
        file.write(str(total_amount))


def power_off_comp(*androids):
    for android in androids:
        android.stop_script()
        android.power_off()
    sleep(30)
    cmd("shutdown /s")


def test():
    androids = instantiate_androids()
    connect_androids()

    total = 0

    for x in range(100):
        start = time.time_ns()
        pix = androids[0].screenshot()
        end = time.time_ns()
        total += (end - start)

    print(total / 100)


def project_recolour():
    img = PIL.Image.open(f"images/map-marker-icon2x.png")

    for x in range(img.width - 1):
        for y in range(img.height - 1):
            if not img.getpixel((x, y)) == (2, 2, 2):
                img.putpixel((x, y), (0, 162, 232))

    img.save("images/map-marker-icon2x.png")


if __name__ == '__main__':
    #calibrate_coordinates()
    main()
    #test()
