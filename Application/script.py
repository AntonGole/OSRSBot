import threading
from Util.helpers import *


class Script:
    def __init__(self, functions, name):
        # Initialize the Script object with a list of functions
        self.functions = functions  # List of functions to be executed as part of the script
        self.started = False  # Flag indicating whether script is started or not
        self.name = name

    def run(self, android):
        self.started = True
        # Iterate through the functions in the script until max_iterations is reached or script is manually stopped
        while android.iterations < android.max_iterations and self.started:
            for function in self.functions:
                execute_function(android, *function)  # Execute each function
            update_info(android)

    def stop(self):
        self.started = False


# Wrapper function for checking if script should be stopped
def execute_function(android, func, *args):
    # Prepares and executes a function with its arguments
    params = list(args)
    params.insert(0, android)  # Add the Android object as the first parameter
    if android.script_stopped:
        android.update_status("Stopped")  # Update status and exit if script is stopped
        exit(0)
    return_value = func(*params)  # Execute the function with the parameters
    if android.script_stopped:
        android.update_status("Stopped")  # Check again if script should stop after function execution
        exit(0)
    return return_value  # Return the function's return value


def update_info(android):
    # Function to update information about the script's execution
    android.iterations += 1  # Increment the iterations count
    # Update the amount label in the GUI
    android.amount_label.configure(text=str(int(android.amount_label.cget("text")) + 1))
    # Calculate and print the runtime of the script
    runtime = " (Runtime: " + str(int((int(time.time()) - int(android.start)) / 3600)) + "h " + str((int(
        (int(time.time()) - int(android.start)) / 60)) % 60) + "m " + str(
        (int(int(time.time()) - int(android.start))) % 60) + "s)"
    print("Iterations " + android.name + ": " + str(android.iterations) + runtime)




