import subprocess
from tkinter import NORMAL

from application.script import *
import PIL.Image


class Android:
    def __init__(self, name, ip, serial, max_iterations, script):
        # Initialize the Android object with various properties
        self.name = name  # Name of the Android VM
        self.serial = serial  # Serial number for ADB
        self.ip = ip  # IP address for ADB connection
        self.max_iterations = max_iterations  # Maximum iterations for the script
        self.script = script  # Script to run
        self.script_stopped = True  # Flag to check if the script is stopped
        self.status_label = None  # Tkinter label to display status
        self.stop_button = None  # Tkinter button to stop the script
        self.iterations = 0  # Counter for the number of iterations
        self.start = 0      # Timestamp when script was started

    def power_on(self):
        # Power on the Android VM using VirtualBox command
        cmd(f"vboxmanage startvm \"{self.name}\"")

    def power_off(self):
        # Power off the Android VM using VirtualBox command
        cmd(f"vboxmanage controlvm \"{self.name}\" poweroff")

    def save_state(self):
        # Save the current state of the Android VM using VirtualBox command
        cmd(f"vboxmanage controlvm \"{self.name}\" savestate")

    def connect(self):
        # Connect to the Android VM using ADB
        commandString = f'cmd /c "adb connect {self.ip}"'
        result = subprocess.run(commandString, shell=True, text=True, capture_output=True)

        # Check for connection errors in the output
        if "cannot resolve host" in result.stdout:
            print(f"Error occurred while connecting: {result.stdout}")
            return False
        return True

    def screenshot(self):
        # Take a screenshot of the Android VM using VirtualBox command
        cmd(f"vboxmanage controlvm \"{self.name}\" screenshotpng images/{self.name[-1]}.png")

        # Open and return the pixel data of the screenshot
        img = PIL.Image.open(f"images/{self.name[-1]}.png")
        pix = img.load()
        return pix

    def input_tap(self, clickX, clickY):
        # Simulate a tap input at the specified coordinates using ADB
        commandString = f'cmd /c "adb -s {self.serial} shell input tap {clickX} {clickY}"'
        os.system(commandString)

    def input_press(self, keyevent):
        # Simulate a key press event using ADB
        commandString = f'cmd /c "adb -s {self.serial} shell input keyevent {keyevent}"'
        os.system(commandString)

    def input_swipe(self, x1, y1, x2, y2, duration):
        # Simulate a swipe input using ADB
        commandString = f'cmd /c "adb -s {self.serial} shell input swipe {x1} {y1} {x2} {y2} {duration}"'
        os.system(commandString)

    def run_script(self):
        # Method to start running the script
        print(f"Script started for {self.name}")
        self.start = time.time()  # Record the start time
        self.update_status("Running")  # Update the status to "Running"

        # Start a separate thread to run a stopwatch for the script
        stopwatch_thread = threading.Thread(
            target=lambda: start_stopwatch(self), args=(), daemon=True)
        stopwatch_thread.start()

        # Run the script in a separate thread
        thread = threading.Thread(target=lambda: self.script.run(self), args=(), daemon=True)
        thread.start()

    def stop_script(self):
        # Stop the running script if the stop button is active
        if self.stop_button["state"] == NORMAL:
            self.stop_button.invoke()

    def update_status(self, text):
        # Update the status text in the Tkinter label
        self.status_label["text"] = text
