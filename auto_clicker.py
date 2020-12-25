from pyautogui import hotkey, press
from time import sleep
from config import click_delay



def click_on_line(line, size=6):
    # hotkey('alt', 'tab')
    sleep(click_delay)
    press('right')
    press('left')

    cords = [0, 0]
    for i in range(len(line)):
        print(f'Цель {line[i]}')
        print(f'коорды до нажания {cords}')

        while cords != line[i]:

            if i % 2 == 0:
                press('right')
                cords[0] = 0 if (cords[0] >= size-1) else (cords[0] + 1)
                if cords in line[:i]:
                    cords[0] += 1
                print('right', cords)

            else:
                press('down')
                cords[1] = 0 if (cords[1] >= size-1) else (cords[1] + 1)
                if cords in line[:i]:
                    cords[1] += 1
                print('down', cords)

        press('enter')
        print(f'коорды после нажания {cords}')
        print()
        sleep(click_delay)
        sleep(0.1)