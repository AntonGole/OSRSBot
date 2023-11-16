from Util.helpers import *


def test_function(android):
    print("test")
    android.input_tap(183, 517)
    android.screenshot()
