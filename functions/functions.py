from utils.helpers import *


def test_function(android):
    android.input_tap(183, 517)
    sleep_random(200, 500)
    android.screenshot()
