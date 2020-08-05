import time

import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
from pynput.keyboard import Key, Listener
from pynput.mouse import Controller, Button
global a_pressed

mouse = Controller()
def get_region():
    global a_pressed
    x1, y1, x2, y2 = 0, 0, 0, 0
    print("Put your mouse in the top-left corner of the puzzles region, then press 'A'")
    cv2.waitKey(0)
    print("wait over")
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()

    if a_pressed:
        print("A pressed")
        a_pressed = False
        x1, y1 = mouse.position

    print("Put your mouse in the bottom-right corner of the puzzles region, then press 'A'")
    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()
    listener.join()

    if a_pressed:
        print("A pressed")
        a_pressed = False
        x2, y2 = mouse.position
    return x1, y1, x2, y2


def on_press(key):
    global a_pressed
    if key.char == 'a':
        a_pressed = True
        return False

    print('{0} pressed'.format(
        key))


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False