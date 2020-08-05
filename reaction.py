import time
import mss
import pynput

mouse = pynput.mouse.Controller()


def on_space(key):
    if key == pynput.keyboard.Key.enter:
        return False


def reaction_test(x1, y1):
    time.sleep(0.3)

    with mss.mss() as sct:
        base = sct.grab({'mon': 1, 'top': y1, 'left': x1, 'width': 1, 'height': 1}).pixel(0, 0)
        while True:

            next = sct.grab({'mon': 1, 'top': y1, 'left': x1, 'width': 1, 'height': 1}).pixel(0, 0)
            diff = base[2] - next[2]
            if diff != 0:
                mouse.click(pynput.mouse.Button.left)
                time.sleep(0.3)
                mouse.click(pynput.mouse.Button.left)
                time.sleep(0.3)
                base = sct.grab({'mon': 1, 'top': y1, 'left': x1, 'width': 1, 'height': 1}).pixel(0, 0)


def start():
    print("Place your mouse in the test area and press 'ENTER' to start.")
    listener = pynput.keyboard.Listener(on_press=on_space)
    listener.start()
    listener.join()
    mouse.click(pynput.mouse.Button.left)
    reaction_test(mouse.position[0], mouse.position[1])
