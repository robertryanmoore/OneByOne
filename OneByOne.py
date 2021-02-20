import pyautogui
from time import  sleep
 
sleep(5)

script = open('script.txt', 'r').read()

for word in script.split():
    sleep(1)
    pyautogui.write(word)
    pyautogui.press("enter")