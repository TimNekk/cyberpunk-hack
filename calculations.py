from image import get_elements, show_path
from math import sqrt
from log import show_notification

"""
1C - 0
55 - 1
BD - 2
E9 - 3
7A - 4
FF - 5
"""


def print_line(line):
    i0, i1, i2, i3, i4, i5, i6, i7, i8 = line
    print(f"({i1}, {i0}) ({i1}, {i2}) ({i3}, {i2}) ({i3}, {i4}) ({i5}, {i4}) ({i5}, {i6}) ({i7}, {i6}) ({i7}, {i8})")


def print_table(table):
    for line in table:
        line_str = ''
        for el in line:
            line_str += str(el['id']) + ' '
        print(line_str)


def get_table():
    table = []
    elements = get_elements(table=True)
    size = int(sqrt(len(elements)))

    i = 0
    for x in range(size):
        line = []
        for y in range(size):
            line.append(elements[i])
            i += 1
        table.append(line)

    return table


def get_reqs():
    reqs = []
    elements = get_elements(table=False)
    req = ''
    current_y = elements[0]['y']
    for element in elements:
        if element['y'] == current_y:
            req += str(element['id'])
        else:
            reqs.append(req)
            req = str(element['id'])
            current_y = element['y']
    reqs.append(req)

    return reqs


def get_best_line(table, reqs, buffer=8, auto_clicker=True):
    line21, line20, line10, line2, line1, line0 = [], [], [], [], [], []
    size = len(table)

    from combinations_generator import get_lines
    lines = get_lines(buffer, size)

    for line in lines:
        # Создание code
        code = ''
        for i in range(buffer-1):
            if i % 2 == 0:
                code += str(table[line[i]][line[i+1]]['id'])
            else:
                code += str(table[line[i+1]][line[i]]['id'])

        # Генерация координат
        cords = []
        if auto_clicker:
            for i in range(buffer-1):
                if i % 2 == 0:
                    cords.append([line[i+1], line[i]])
                else:
                    cords.append([line[i], line[i+1]])
        else:
            for i in range(buffer-1):
                if i % 2 == 0:
                    cords.append(table[line[i]][line[i+1]])
                else:
                    cords.append(table[line[i+1]][line[i]])

        # Если взлом протокола
        if len(reqs) == 1:
            if reqs[0] in code:
                print('Взлом протокола')
                show_notification('Взлом протокола', '')
                return cords
            else:
                continue

        # Присутсвие нужных комбинаций в code
        is0 = reqs[0] in code
        is1 = reqs[1] in code
        is2 = reqs[2] in code

        if is0 and is1 and is2:
            # Нашли все 3 комбинации
            show_notification('3 и 2 и 1', 'Добыча данных')
            print('line321')
            return cords
        elif is2 and is1:
            line21 = cords
        elif is2 and is0:
            line20 = cords
        elif is1 and is0:
            line10 = cords
        elif is2:
            line2 = cords
        elif is1:
            line1 = cords
        elif is0:
            line0 = cords

    if line21:
        print('line21')
        show_notification('3 и 2', 'Добыча данных')
        return line21
    elif line20:
        print('line20')
        show_notification('3 и 1', 'Добыча данных')
        return line20
    elif line10:
        print('line10')
        show_notification('2 и 1', 'Добыча данных')
        return line10
    elif line2:
        print('line2')
        show_notification('3', 'Добыча данных')
        return line2
    elif line1:
        print('line1')
        show_notification('2', 'Добыча данных')
        return line1
    elif line0:
        print('line0')
        show_notification('1', 'Добыча данных')
        return line0