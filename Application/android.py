from tkinter import NORMAL

from Application.script import *
import PIL.Image


class Android:
    def __init__(self, name, serial, ip, amount, script_functions, script_number):
        self.name = name
        self.serial = serial
        self.ip = ip
        self.amount = amount
        self.script_functions = script_functions
        self.script_number = script_number

        self.start = 0
        self.cooking_fails = 0
        self.cooked_amount = 0
        self.status = "Banking"
        self.script_stopped = True

        self.status_label = None
        self.stop_button = None

        # For ardougne agility
        # self.pie_number = 3
        # self.lap_number = 0
        self.pickup = False

    def power_on(self):
        cmd(f"vboxmanage startvm \"{self.name}\"")

    def power_off(self):
        cmd(f"vboxmanage controlvm \"{self.name}\" poweroff")

    def save_state(self):
        cmd(f"vboxmanage controlvm \"{self.name}\" savestate")

    def start_osrs(self):
        self.input_tap(150, 188)

    def connect(self):
        commandString = f'cmd /c "adb connect {self.ip}"'
        os.system(commandString)
        sleep(1)

    def screenshot(self):
        cmd(f"vboxmanage controlvm \"{self.name}\" screenshotpng images/{self.name[-1]}.png")

        img = PIL.Image.open(f"images/{self.name[-1]}.png")
        pix = img.load()
        #os.remove(f"images/{self.name[-1]}.png")
        return pix

    def input_tap(self, clickX, clickY):
        commandString = f'cmd /c "adb -s {self.serial} shell input tap {clickX} {clickY}"'
        os.system(commandString)

    def input_press(self, keyevent, t1, t2):
        commandString = f'cmd /c "adb -s {self.serial} shell input keyevent {keyevent}"'
        os.system(commandString)
        if t2:
            sleep(randint(t1, t2) / 1000)

    def input_swipe(self, x1, y1, x2, y2, time):
        commandString = f'cmd /c "adb -s {self.serial} shell input swipe {x1} {y1} {x2} {y2} {time}"'
        os.system(commandString)

    def run_script(self):
        # If mining script, start screenshot thread
        # if self.script_number == 6:
        #     thread = threading.Thread(
        #         target=lambda: self.start_mining_screenshot_thread(), args=(), daemon=True)
        #     thread.start()

        script = Script(self.script_functions, self)
        thread = threading.Thread(
            target=lambda: script.run(), args=(), daemon=True)
        thread.start()

    def stop_script(self):
        if self.stop_button["state"] == NORMAL:
            self.stop_button.invoke()

    def start_mining_screenshot_thread(self):
        while True:
            sleep(0.01)
            pix = self.screenshot()

            # Check if iron ore 1 is up
            if add_color_margin(pix[554, 653], 54, 31, 22, 10):
                self.ore_1 = True
            else:
                self.ore_1 = False

            # Check if iron ore 2 is up
            if add_color_margin(pix[349, 514], 38, 22, 17, 10):
                self.ore_2 = True
            else:
                self.ore_2 = False

            # Check if iron ore 3 is up
            if add_color_margin(pix[675, 545], 45, 25, 18, 10):
                self.ore_3 = True
            else:
                self.ore_3 = False