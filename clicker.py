from pyautogui import hotkey, press
from time import sleep
from config import click_delay


def modify_cord(axis, size, cords, line, step, check=False):
    if cords[axis] >= size - 1:
        cords[axis] = 0
    elif not check:
        cords[axis] += 1

    # Координата уже была нажата
    if cords in line[:step]:
        cords[axis] += 1
        print('Рекурсия')
        cords = modify_cord(axis, size, cords, line, step, check=True)

    return cords


def click_on_line(line, size=6, alt_tab=False):
    if alt_tab:
        hotkey('alt', 'tab')

    sleep(click_delay)
    press('right')
    press('left')

    cords = [0, 0]
    for step in range(len(line)):
        print(f'Цель {line[step]}\nКорды до нажания {cords}')

        while cords != line[step]:

            if step % 2 == 0:
                press('right')
                cords = modify_cord(0, size, cords, line, step)
                print('right', cords)
            else:
                press('down')
                cords = modify_cord(1, size, cords, line, step)
                print('down', cords)

                # press('down')
                # cords[1] = 0 if (cords[1] >= size-1) else (cords[1] + 1)
                # if cords in line[:i]:
                #     cords[1] += 1
                # print('down', cords)

        press('enter')
        print(f'Корды после нажания {cords}\n')
        sleep(click_delay)