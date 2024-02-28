import pyautogui
from time import sleep

sleep(5)

currentMouseX, currentMouseY = pyautogui.position()

print(currentMouseX, currentMouseY)