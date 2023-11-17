# OSRSBot

OSRSBot is a Python-based automation tool for controlling Android Virtual Machines via ADB (Android Debug Bridge) and VirtualBox. It provides a graphical user interface for managing multiple Android VMs, allowing for the automation of tasks and scripts.


## Screenshots

### Single Android Instance

![Single Android Instance](/screenshots/SingleAndroid.png)

This screenshot shows the application running with a single Android instance.

### Multiple Android Instances

![Multiple Android Instances](/screenshots/MultipleAndroids.png)

This screenshot demonstrates the application managing multiple Android instances.

## Getting Started

These instructions will guide you on how to set up and run OSRSBot on your local machine for development and testing purposes.

### Prerequisites

Before installing OSRSBot, ensure you have the following installed:
- Python 3.8 or later
- PIL (Python Imaging Library)
- Tkinter (Python's standard GUI package)
- VirtualBox running Android-x86
- Android Debug Bridge (ADB)

### Installation

1. **Clone the Repository**

   To get started, clone the repository to your local machine:
   ```
   git clone https://github.com/AntonGole/OSRSBot
   cd OSRSBot
   ```

2. **Install Required Python Libraries**

   Install the necessary Python libraries using pip:
   ```
   pip install Pillow
   ```
   Note: Tkinter usually comes pre-installed with Python. If not, install it using your system's package manager.

3. **Configure VirtualBox and ADB**

   Ensure that VirtualBox VMs are set up correctly and ADB is configured to connect to them.

### Usage

1. **Running the Application**

   Execute the `main.py` script to start the application:
   ```
   python main.py
   ```

2. **Using the Application**

   - Create your own scripts to use or try out the test script already implemented.
   - Input the details of the Android VMs when prompted.
   - Use the GUI to start/stop scripts and monitor their status.

## Dependencies

- Python 3.x: The core language used.
- Pillow: For image processing tasks.
- Tkinter: For the graphical user interface.
- VirtualBox: For managing Android VMs.
- ADB: For communicating with Android VMs.

## License

This project is licensed under the [MIT License](LICENSE).
