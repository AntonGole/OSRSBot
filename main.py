import Util.calibration as calibrations

from Application.script import *

from Application.app import App

from Application.android import Android

from PIL import Image

test_script = [
    [OSRS_test]
]


def instantiate_androids():
    android = Android("Android 4", "192.168.0.246:5555", "192.168.0.246", 10000, test_script)
    return [android]


def connect_androids():
    androids = instantiate_androids()
    cmd("adb disconnect")
    sleep(3)
    cmd("adb kill-server")
    sleep(3)

    for android in androids:
        android.connect()


def main():
    androids = instantiate_androids()
    #connect_androids()
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
