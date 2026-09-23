from machine import Pin
from neopixel import NeoPixel
from time import sleep
import random

PIXELS: int = 36
np = NeoPixel(Pin(14), PIXELS)

def n1() -> None:
    c: int = 0

    while True:
        for i in range(c%2, PIXELS, 2):
            np[i] = (255, 0, 0)

        for i in range((c+1)%2, PIXELS, 2):
            np[i] = (0, 0, 255)

        np.write()
        sleep(1)

        c += 1


def n2() -> None:
    SEG_LEN: int = PIXELS//4
    while True:
        for seg in range(0, PIXELS, 4):
            for i in range(PIXELS):
                np[i] = (0, 0, 0)

            for i in range(seg, seg+SEG_LEN):
                np[i] = (255, 0, 0)
            np.write()

            sleep(1)

def n3() -> None:
    def draw_board() -> None:
        for i in range(0, PIXELS, 2):
            np[i] = (255, 0, 0)

        for i in range(1, PIXELS, 2):
            np[i] = (0, 0, 0)

        np[0] = (0, 255, 0)

    
    random_num: int = random.randrange(0, 16)

    for _ in range(random.randrange(1, 3)):
        for i in range(PIXELS):
            draw_board()
            np[i] = (255, 255, 255)

            np.write()
            sleep(1/PIXELS)
    
    for i in range(random_num):
        draw_board()
        np[i] = (255, 255, 255)

        np.write()
        sleep(1/PIXELS)


if __name__ == "__main__":
    n3()
