import time

import pyautogui as pag

pag.FAILSAFE=False

mins = 2

total_time = time.time() + 60 * mins

while True:

    search_bar_pos= (111,1050)
    pag.moveTo(search_bar_pos)
    pag.click()

    time.sleep(15)
    pag.typewrite('Notepad', 0.25)
    pag.press('enter')
    
    while time.time() <= total_time:
        time.sleep(15)
        pag.typewrite("Boring Work! Don't do.\n", 0.25)
        time.sleep(15)
    break