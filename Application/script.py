import threading
from Util.helpers import *


class Script:
    def __init__(self, functions, android):
        self.functions = functions
        self.android = android

    def run(self):
        print(f"Script started for {self.android.name}")
        self.android.start = time.time()
        self.android.update_status("Running")
        stopwatch_thread = threading.Thread(
            target=lambda: start_stopwatch(self.android), args=(), daemon=True)
        stopwatch_thread.start()

        while self.android.iterations < self.android.max_iterations:
            for function in self.functions:
                execute(self.android, *function)


# Wrapper function for checking if script should be stopped
def execute(android, func, *args):
    params = list(args)
    params.insert(0, android)
    if android.script_stopped:
        android.update_status("Stopped")
        exit(0)
    return_value = func(*params)
    if android.script_stopped:
        android.update_status("Stopped")
        exit(0)
    return return_value


def update_info(android):
    android.iterations += 1
    android.amount_label.configure(text=str(int(android.amount_label.cget("text")) + 1))
    iterations_per_hour = " (" + str(
        int(android.iterations / ((int(time.time()) - int(android.start)) / 3600))) + " iterations/h)"
    runtime = " (Runtime: " + str(int((int(time.time()) - int(android.start)) / 3600)) + "h " + str((int(
        (int(time.time()) - int(android.start)) / 60)) % 60) + "m " + str(
        (int(int(time.time()) - int(android.start))) % 60) + "s)"
    print("Iterations " + android.name + ": " + str(android.iterations) + iterations_per_hour + runtime)
