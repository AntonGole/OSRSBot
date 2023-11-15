from osrs.functions import *
import random as random
import time
import threading


class Script:
    def __init__(self, functions, android):
        self.functions = functions
        self.last_login = 0
        self.login_time = 0
        self.android = android

    def run(self):
        self.setup(True)

        while self.android.cooked_amount < self.android.amount:
            for function in self.functions:
                execute(self.android, *function)



            # Automatic logout and login
            # REMOVE CONTINUE STATEMENT TO IMPLEMENT LOGOUT FUNCTION
            continue

            if (time.time() - self.last_login) > self.login_time:
                print("Logging out")
                self.logout()

            # For ardy agility
            # if (time.time() - self.last_login) > self.login_time:
            #     self.android.pickup = True
            #     for function in self.functions:
            #         execute(self.android, *function)
            #     self.android.pickup = False
            #     print("Logging out")
            #     self.logout()

    def setup(self, first):
        if first:
            self.android.start = time.time()
        self.last_login = time.time()
        self.login_time = randint(16200000, 20880000) / 1000
        #self.login_time = randint(10000, 20000) / 1000

        timer_thread = threading.Thread(
            target=lambda: update_timer(int(self.login_time), self.android), args=(), daemon=True)
        timer_thread.start()
        if first:
            stopwatch_thread = threading.Thread(
                target=lambda: stopwatch(self.android), args=(), daemon=True)
            stopwatch_thread.start()

        execute(self.android, setup)

    def logout(self):
        #execute(self.android, OSRS_logout, 240000, 420000, False)
        execute(self.android, OSRS_logout, 120000, 240000, False)
        execute(self.android, OSRS_login, 800, 1500, False)
        self.android.timer_stop = False

        self.setup(False)
        #execute(self.android, OSRS_agility_ardy_pick_up_marks)


# Wrapper function for checking if script should be stopped
def execute(android, func, *args):
    params = list(args)
    params.insert(0, android)
    if android.script_stopped:
        android.status_label["text"] = "Stopped"
        exit(0)
    return_value = func(*params)
    if android.script_stopped:
        android.status_label["text"] = "Stopped"
        exit(0)
    return return_value


def update_info(android, increase):
    if android.script_number == 5:
        print()
        android.cooked_amount += increase
        android.amount_label.configure(text=str(int(android.amount_label.cget("text")) + increase))
        cooks_per_hour = " (" + str(
            int(android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) + " laps/h)"
        runtime = " (Runtime: " + str(int((int(time.time()) - int(android.start)) / 3600)) + "h " + str((int(
            (int(time.time()) - int(android.start)) / 60)) % 60) + "m " + str(
            (int(int(time.time()) - int(android.start))) % 60) + "s)"
        print("Laps ran " + android.name + ": " + str(android.cooked_amount) + cooks_per_hour + runtime)
        print("Xp/h: " + str(int((android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) * 570))
        print("Xp gained: " + str(android.cooked_amount * 570))
        print()

    elif android.script_number == 1:
        android.cooked_amount += increase
        android.amount_label.configure(text=str(int(android.amount_label.cget("text")) + increase))
        cooks_per_hour = " (" + str(
            int(android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) + " bows/h)"
        runtime = " (Runtime: " + str(int((int(time.time()) - int(android.start)) / 3600)) + "h " + str((int(
            (int(time.time()) - int(android.start)) / 60)) % 60) + "m " + str(
            (int(int(time.time()) - int(android.start))) % 60) + "s)"
        print("Resources " + android.name + ": " + str(android.cooked_amount) + cooks_per_hour + runtime)
        print("Xp/h: " + str(int((android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) * 180))

    elif android.script_number == 7:
        print()
        android.cooked_amount += increase
        android.amount_label.configure(text=str(int(android.amount_label.cget("text")) + increase))
        cooks_per_hour = " (" + str(
            int(android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) + " laps/h)"
        runtime = " (Runtime: " + str(int((int(time.time()) - int(android.start)) / 3600)) + "h " + str((int(
            (int(time.time()) - int(android.start)) / 60)) % 60) + "m " + str(
            (int(int(time.time()) - int(android.start))) % 60) + "s)"
        print("Laps ran " + android.name + ": " + str(android.cooked_amount) + cooks_per_hour + runtime)
        print("Xp/h: " + str(int((android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) * 793))
        print("Xp gained: " + str(android.cooked_amount * 793))
        print()
    else:
        android.cooked_amount += increase
        android.amount_label.configure(text=str(int(android.amount_label.cget("text")) + increase))
        cooks_per_hour = " (" + str(int(android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) + " cooks/h)"
        runtime = " (Runtime: " + str(int((int(time.time()) - int(android.start)) / 3600)) + "h " + str((int(
            (int(time.time()) - int(android.start)) / 60)) % 60) + "m " + str((int(int(time.time()) - int(android.start))) % 60) + "s)"
        print("Resources " + android.name + ": " + str(android.cooked_amount) + cooks_per_hour + runtime)
        print("Xp/h: " + str(int((android.cooked_amount / ((int(time.time()) - int(android.start)) / 3600))) * 150))


def log_amount(name):
    with open(f"logs/{name[-1]}.txt", "r+") as file:
        logged_amount = file.readline()
        file.seek(0)
        file.write(str(int(logged_amount) + 28))


def wait(android, t1, t2):
    sleep(randint(t1, t2) / 1000)


def wait_anti_ban(android, t1, t2, t3, t4, chance):
    if random.randint(0, chance) == 50:
        print("Adding extra delay: " + android.name)
        sleep(randint(t3, t4) / 1000)
    else:
        sleep(randint(t1, t2) / 1000)
