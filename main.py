from Application.script import *

from Application.app import App

from Application.android import Android

from osrs.functions import *

test = Script([[test_function]], "example")


def instantiate_androids(androids_info):
    androids = []
    for android in androids_info:
        a = Android(android['title'], android['ip_address'], android['serial_number'], 10000, test)
        androids.append(a)
    return androids


def connect_androids(androids):
    for android in androids:
        if not android.connect():
            return False
    return True


def main():
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

    androids = instantiate_androids(androids_info)

    if connect_androids(androids):
        print("Success! Application started.\n")
        app = App(androids)
        app.run()
    else:
        print("Make sure the info you are typing is correct.\n")
        main()


if __name__ == '__main__':
    main()
