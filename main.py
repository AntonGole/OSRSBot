from application.script import *

from application.app import App

from application.android import Android

from functions.functions import *

test = Script([[test_function]], "example")  # Initialize a test script


def instantiate_androids(androids_info):
    # Create and return Android objects from provided info
    androids = []
    for android in androids_info:
        a = Android(android['title'], android['ip_address'], android['serial_number'], 10000, test)
        androids.append(a)
    return androids


def connect_androids(androids):
    # Connect to all Android instances, return False if any connection fails
    for android in androids:
        if not android.connect():
            return False
    return True


def main():
    # Main function to run the application

    androids_info = []
    while True:
        # Ask the user for the title of the Android machine
        title = input("Please input the title of the Android machine: ")

        # Ask the user for the IP address of the Android machine
        ip_address_input = input(f"Please input ip address of Android machine '{title}': ")

        # Remove spaces from the input
        ip_address = ip_address_input.replace(" ", "")

        # Create another string for the serial number and append ":5555" to it
        serial_number = ip_address + ":5555"

        # Store the details in a dictionary and add it to the list
        android_details = {
            "title": title,
            "ip_address": ip_address,
            "serial_number": serial_number
        }
        androids_info.append(android_details)

        # Ask the user if they want to register more androids
        continue_input = input("Do you want to register more androids? (Y/N): ")
        if continue_input.upper() != 'Y':
            break

    # Instantiate Android objects based on user-provided information
    androids = instantiate_androids(androids_info)

    # Attempt to establish connections with all instantiated Android devices
    if connect_androids(androids):
        # If all Android devices are successfully connected, start the application
        print("Success! Application started.\n")
        app = App(androids)  # Initialize the main application with connected Android devices
        app.run()  # Run the application's main loop
    else:
        # If any Android device fails to connect, prompt the user to check the information entered
        print("Make sure the info you are typing is correct.\n")
        main()  # Restart the main function for user to re-enter information


if __name__ == '__main__':
    main()
