from functools import partial
from tkinter import *
from tkinter.font import Font
import tkinter.font as font
from osrs.functions import *
from PIL import Image, ImageTk


class App(Tk):
    def __init__(self, androids):
        super().__init__()
        self.title('OSRS Bot')
        self.geometry(f"{236 * len(androids)}x413")
        self.resizable(False, False)
        self.configure(bg='#1D2025')

        self.frames = []
        self.start_buttons = []
        self.stop_buttons = []
        self.reset_buttons = []
        self.image_labels = []

        self.add_options()

        # move window center
        winWidth = self.winfo_reqwidth()
        winwHeight = self.winfo_reqheight()
        posRight = int(self.winfo_screenwidth() / 2 - winWidth / 2)
        posDown = int(self.winfo_screenheight() / 2 - winwHeight / 2)
        self.geometry("+{}+{}".format(posRight, posDown))

        frm = Frame(self, bg='#1D2025')
        frm.grid()

        # Create labels and buttons for every android object created
        for index, android in enumerate(androids):
            android_frame = Frame(frm)
            if (index % 2) == 0:
                android_frame.configure(bg='#1D2025')
            else:
                android_frame.configure(bg='#24272C')
            android_frame.grid(row=0, column=index)

            # Name label, shows name of android
            Label(android_frame, text=f"{android.name}", width=8).grid(column=0, row=0, columnspan=2, pady=(10, 0), padx=(10, 10))

            # Amount labels,
            amount_label_info = Label(android_frame, text="Count:", width=8)
            amount_label_info.grid(column=0, row=2, pady=(0, 0), padx=(10, 10))
            amount_label = Label(android_frame, text="0", width=8, relief=SUNKEN)
            amount_label.grid(column=1, row=2, pady=(0, 0), padx=(10, 10))
            android.amount_label = amount_label

            # Stopwatch labels, shows runtime of script for android
            stopwatch_label_info = Label(android_frame, text="Runtime:", width=8)
            stopwatch_label_info.grid(column=0, row=3, pady=(10, 0), padx=(10, 10))
            stopwatch_label = Label(android_frame, text="0:00:00", width=8, relief=SUNKEN)
            stopwatch_label.grid(column=1, row=3, pady=(10, 0), padx=(10, 10))
            android.stopwatch_label = stopwatch_label

            # status labels, shows status of android
            status_label_info = Label(android_frame, text="Status:", width=8)
            status_label_info.grid(column=0, row=4, pady=(10, 0), padx=(10, 10))
            status_label = Label(android_frame, text="Stopped", width=8, relief=SUNKEN)
            status_label.grid(column=1, row=4, pady=(10, 0), padx=(10, 10))
            android.status_label = status_label

            # Start button, start script for android
            start_button = Button(android_frame, text="Start", command=partial(self.start_button_function, index, android),
                                  bg="#BB86FC", height=1, width=8, disabledforeground="#404040")
            start_button.grid(column=0, row=5, padx=(10, 10), pady=(10, 0), columnspan=1)
            start_button.bind('<Enter>', lambda event, high=True: toggle_button_highlight(event, high))
            start_button.bind('<Leave>', lambda event, high=False: toggle_button_highlight(event, high))

            # Stop button, stop script for android
            stop_button = Button(android_frame, text="Stop", command=partial(self.stop_button_function, index, android),
                                 bg="#5e5e5e", height=1, width=8, disabledforeground="#404040")
            stop_button.grid(column=1, row=5, padx=(10, 10), pady=(10, 0), columnspan=1)
            stop_button.bind('<Enter>', lambda event, high=True: toggle_button_highlight(event, high))
            stop_button.bind('<Leave>', lambda event, high=False: toggle_button_highlight(event, high))
            stop_button["state"] = DISABLED
            android.stop_button = stop_button
            myFont = font.Font(size=7)

            # Reset button, reset amount label
            reset_button = Button(android_frame, text="Reset", command=android.amount_label.configure(text="0"),
                                  bg="#BB86FC", height=1, width=10, font=myFont)
            reset_button.grid(column=1, row=1, padx=(10, 10), pady=(10, 0), sticky=E)
            reset_button.bind('<Enter>', lambda event, high=True: toggle_button_highlight(event, high))
            reset_button.bind('<Leave>', lambda event, high=False: toggle_button_highlight(event, high))

            # Android image label
            cmd(f"vboxmanage controlvm \"{android.name}\" screenshotpng label_images/{android.name[-1]}.png")
            img = Image.open(f"label_images/{android.name[-1]}.png")
            img = img.resize((229, 172), Image.ANTIALIAS)
            new_image = ImageTk.PhotoImage(img)
            label = Label(frm, image=new_image)
            label.grid(column=index, row=6)
            label.image = new_image

            # Add all buttons and labels to the window
            self.start_buttons.append(start_button)
            self.stop_buttons.append(stop_button)
            self.reset_buttons.append(reset_button)
            self.image_labels.append(label)

    # Start the tkinter application
    def run(self):
        self.mainloop()

    # Add styles to the UI
    def add_options(self):
        default_font = Font(family="Helvetica", size=15)
        self.option_add("*Font", default_font)
        self.option_add("*Label.background", '#2E2E2E')
        self.option_add("*Label.foreground", '#D3CEC4')
        self.option_add("*Entry.background", '#2E2E2E')
        self.option_add("*Entry.foreground", '#D3CEC4')
        self.option_add('*TCombobox*Listbox.background', '#2E2E2E')
        self.option_add('*TCombobox*Listbox.foreground', '#D3CEC4')
        self.option_add('*TCombobox*Listbox.selectBackground', '#454545')
        self.option_add('*TCombobox*Listbox.selectForeground', '#D3CEC4')
        self.option_add("*Button.activebackground", '#BB86FC')

    # Method called when clicking the start button
    def start_button_function(self, index, android):
        disable_buttons(self.start_buttons[index])
        enable_buttons(self.stop_buttons[index])
        android.script_stopped = False
        android.run_script()

    # Method called when clicking the stop button
    def stop_button_function(self, index, android):
        disable_buttons(self.stop_buttons[index])
        android.status_label["text"] = "Stopping"
        android.script_stopped = True
        thread = threading.Thread(
            target=lambda: stop_script(self, index, android), args=(), daemon=True)
        thread.start()


# Enable specified button
def enable_buttons(*buttons):
    for button in buttons:
        button.configure(bg="#BB86FC", state=NORMAL, cursor="hand2")


# Disable specified button
def disable_buttons(*buttons):
    for button in buttons:
        button.configure(bg="#5e5e5e", state=DISABLED, cursor="arrow")


def toggle_button_highlight(event, high):
    if high and event.widget["state"] == NORMAL:
        event.widget["bg"] = "#cea6ff"
    if not high and event.widget["state"] == NORMAL:
        event.widget["bg"] = "#BB86FC"


def manual_logout(app, index, android):
    OSRS_logout(android, 800, 1500, True)
    app.enable_buttons(app.login_buttons[index])


def manual_login(app, index, android):
    OSRS_login(android, 800, 1500, True)
    app.enable_buttons(app.logout_buttons[index], app.start_buttons[index])


def stop_script(app, index, android):
    while True:
        if android.status_label["text"] == "Stopped":
            break
        sleep(0.1)
    app.enable_buttons(app.start_buttons[index])
