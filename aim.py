import time
import cv2
import numpy as np
from pynput.keyboard import Key, Listener
from pynput.mouse import Controller, Button
import mss

global a_pressed
global mouse


def get_region():
    global mouse
    global a_pressed
    x1, y1, x2, y2 = 0, 0, 0, 0
    print("Put your mouse in the top-left corner of the puzzles region, then press 'A'")
    listener = Listener(on_press=on_press)
    listener.start()
    listener.join()
    if a_pressed:
        print("A pressed")
        a_pressed = False
        x1, y1 = mouse.position

    print("Put your mouse in the bottom-right corner of the puzzles region, then press 'A'")
    listener = Listener(on_press=on_press)
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


def aim_test(x1, y1, x2, y2):
    global mouse
    time.sleep(0.3)
    template = cv2.imread("aim_target.png", -1)
    grey = cv2.cvtColor(template, cv2.COLOR_BGRA2GRAY)
    w, h = grey.shape[::-1]
    clicks = 0
    with mss.mss() as sct:
        while clicks <= 30:
            pic = np.array(sct.grab({'mon': 1, 'top': y1, 'left': x1, 'width': x2 - x1, 'height': y2 - y1}))

            res = cv2.matchTemplate(pic, template, cv2.TM_CCOEFF)
            _, _, _, max_loc = cv2.minMaxLoc(res)
            center = (max_loc[0] + (round((w / 2))), max_loc[1] + (round(h / 2)))

            mouse.position = (x1 + center[0], y1 + center[1])
            mouse.click(Button.left)
            mouse.position = (x1, y1)
            time.sleep(0.05)
            clicks += 1


def start():
    global mouse
    mouse = Controller()
    x1, y1, x2, y2 = get_region()
    aim_test(x1, y1, x2, y2)
