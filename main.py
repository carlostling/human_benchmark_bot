import os

import pynput

import aim
import reaction
import type_test


def quit_program(key):
    if key == pynput.keyboard.Key.esc:
        os._exit(1)


tests = {1: "Reaction", 2: "Aim", 3: "Typing"}

print("At any time, you can press 'ESC' to quit this program")
listener = pynput.keyboard.Listener(on_press=quit_program)
listener.start()

for key, value in tests.items():
    print("{}: {}".format(key, value))

test_num = int(input("Select your test by writing its number and hitting 'ENTER'\n"))



switcher = {
    1: reaction.start,
    2: aim.start,
    3: type_test.start
}
test_start = switcher.get(test_num, lambda: "Invalid test - quitting.")
test_start()

