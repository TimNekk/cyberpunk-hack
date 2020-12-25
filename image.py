from PIL import Image, ImageDraw
from pyautogui import locateAllOnScreen, screenshot, center
from config import *
from operator import itemgetter


def show_found(image: Image, file: str):
    image_draw = ImageDraw.Draw(image)
    i = 1
    for location in locateAllOnScreen(file, confidence=0.94):
        cords = [location[0], location[1], location[0] + location[2], location[1] + location[3]]
        print(cords[1])
        image_draw.rectangle(cords)
        image_draw.text((location[0] - 25, location[1] - 5), str(i), font=font)
        i += 1

    image.show()


def get_elements_with_rectangles(image: Image):
    image_draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20)

    elements = []
    j = 1
    used_y = []
    for i, reference in enumerate(references_table):
        for location in locateAllOnScreen(reference['img'], confidence=reference['confidence'], grayscale=True):
            cords = center(location)

            print(cords.y)
            print(used_y)

            if not used_y:
                used_y.append(cords.y)
            closest_y = min(used_y, key=lambda a: abs(a - cords.y))
            if (closest_y - 5) < cords.y < (closest_y + 5):
                cords_y = closest_y
            else:
                cords_y = cords.y
                used_y.append(cords.y)

            print(cords_y)
            print()

            element = {'id': i,
                       'x': cords.x,
                       'y': cords_y}

            if element not in elements:
                elements.append(element)

                cords = [location[0], location[1], location[0] + location[2], location[1] + location[3]]
                image_draw.rectangle(cords)
                image_draw.text((location[0] - 25, location[1] - 5), str(j), font=font)
                j += 1

    # if len(elements) not in elements_size:
    #     raise ValueError (f'Найдено {len(elements)} элементов')
    elements = sorted(elements, key=itemgetter('y', 'x'))

    print(elements)
    print(len(elements))

    elements_small = []
    j = 1
    for i, reference in enumerate(references_reqs):
        for location in locateAllOnScreen(reference['img'], confidence=reference['confidence']):
            cords = center(location)
            element = {'id': i,
                       'x': cords.x,
                       'y': cords.y}
            elements_small.append(element)

            cords = [location[0], location[1], location[0] + location[2], location[1] + location[3]]
            image_draw.rectangle(cords, outline='red')
            image_draw.text((location[0] - 25, location[1] - 5), str(j), font=font)
            j += 1

    elements_small = sorted(elements_small, key=itemgetter('y', 'x'))

    print(elements_small)
    print(len(elements_small))
    image.show()


def get_elements(table: bool):
    references = references_table if table else references_reqs
    elements = []
    used_y = []
    for i, reference in enumerate(references):
        for location in locateAllOnScreen(reference['img'], confidence=reference['confidence'], grayscale=True):
            cords = center(location)

            if not used_y:
                used_y.append(cords.y)
            closest_y = min(used_y, key=lambda a: abs(a - cords.y))
            if (closest_y - 5) < cords.y < (closest_y + 5):
                cords_y = closest_y
            else:
                cords_y = cords.y
                used_y.append(cords.y)

            element = {'id': i,
                       'x': cords.x,
                       'y': cords_y}

            if element not in elements:
                elements.append(element)

    if len(elements) not in elements_size and table:
        from log import show_notification
        show_notification('Ошибка', f'Найдено {len(elements)} элементов')

        raise ValueError (f'Найдено {len(elements)} элементов')

    elements = sorted(elements, key=itemgetter('y', 'x'))

    for element in elements:
        print(element)
    print(len(elements))
    return elements


def show_path(line):
    image = screenshot()
    image_draw = ImageDraw.Draw(image)

    for i in range(len(line)-1):
        if i % 2 == 0:
            image_draw.polygon((line[i]['x']+5, line[i]['y'], line[i]['x']-5, line[i]['y'], line[i+1]['x'], line[i+1]['y']), fill='white')
        else:
            image_draw.polygon((line[i]['x'], line[i]['y']+5, line[i]['x'], line[i]['y']-5, line[i+1]['x'], line[i+1]['y']), fill='white')
        image_draw.text((line[i]['x'], line[i]['y']), str(i + 1), font=font)
    image_draw.text((line[-1]['x'], line[-1]['y']), str(len(line)), font=font)

    image.show()


if __name__ == '__main__':
    # get_elements(screenshot())
    get_elements_with_rectangles(screenshot())
    # show_found(screenshot(), 'assets/55.png')
