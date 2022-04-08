# file name key_press

from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
import webbrowser
import pyautogui
from playsound import playsound
from crop_image import crop
from ocr_from import get_string

FILE_NAME = "monkey.png"

webbrowser.open('https://monkeytype.com/', new=2)

keyboard = Controller()

sleep(4.5)

playsound('bip.wav')

myScreenshot = pyautogui.screenshot()
myScreenshot.save(FILE_NAME)
cropped_file = crop(FILE_NAME)


words = get_string(cropped_file).replace("\n", " ")

sleep(1)


def key_generator(_words):
    for letter in _words:
        keyboard.press(letter)
        keyboard.release(letter)
        t = uniform(0.02, 0.08)
        sleep(0.04)
        sleep(uniform(0.09, 0.13)) if t > 0.075 else None


key_generator(words)
print(repr(words))