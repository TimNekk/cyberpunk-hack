from image import get_elements, show_path
from math import sqrt
from log import show_notification

"""
1C - 0
55 - 1
BD - 2
E9 - 3
7A - 4
"""


def print_line(line):
    i0, i1, i2, i3, i4, i5, i6, i7, i8 = line
    print(f"({i1}, {i0}) ({i1}, {i2}) ({i3}, {i2}) ({i3}, {i4}) ({i5}, {i4}) ({i5}, {i6}) ({i7}, {i6}) ({i7}, {i8})")


# table = [[0, 0, 1, 2, 3],
#          [2, 0, 2, 1, 2],
#          [2, 3, 1, 0, 1],
#          [1, 0, 2, 0, 3],
#          [3, 3, 0, 3, 1]]


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


# reqs = ['342',
#         '21',
#         '43']


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


def get_best_line(table, reqs, auto_clicker=True):
    line21, line20, line10, line2, line1, line0 = [], [], [], [], [], []

    i0 = 0
    for i1 in range(len(table)):
        buffer_temp = 8
        while buffer_temp != 0:

            for i2 in range(len(table)):
                if i2 == i0:
                    continue

                for i3 in range(len(table)):
                    if i3 == i1:
                        continue

                    for i4 in range(len(table)):
                        if i4 == i2:
                            continue

                        for i5 in range(len(table)):
                            if i5 == i3:
                                continue

                            for i6 in range(len(table)):
                                if i6 == i4:
                                    continue

                                for i7 in range(len(table)):
                                    if i7 == i5:
                                        continue

                                    for i8 in range(len(table)):
                                        i_all = ((i1, i0), (i1, i2), (i3, i2), (i3, i4), (i5, i4), (i5, i6), (i7, i6), (i7, i8))

                                        if i8 == i6 or len(i_all) != len(set(i_all)):
                                            continue

                                        code = f"{table[i0][i1]['id']}" \
                                               f"{table[i2][i1]['id']}" \
                                               f"{table[i2][i3]['id']}" \
                                               f"{table[i4][i3]['id']}" \
                                               f"{table[i4][i5]['id']}" \
                                               f"{table[i6][i5]['id']}" \
                                               f"{table[i6][i7]['id']}" \
                                               f"{table[i8][i7]['id']}"

                                        if auto_clicker:
                                            line = (
                                            [i1, i0], [i1, i2], [i3, i2], [i3, i4], [i5, i4], [i5, i6], [i7, i6],
                                            [i7, i8])
                                        else:
                                            line = [table[i0][i1],
                                                    table[i2][i1],
                                                    table[i2][i3],
                                                    table[i4][i3],
                                                    table[i4][i5],
                                                    table[i6][i5],
                                                    table[i6][i7],
                                                    table[i8][i7]]

                                        if len(reqs) == 1:
                                            if reqs[0] in code:
                                                print('Взлом протокола')
                                                show_notification('Взлом протокола', '')
                                                return line
                                            else:
                                                continue

                                        is0 = reqs[0] in code
                                        is1 = reqs[1] in code
                                        is2 = reqs[2] in code

                                        if is0 and is1 and is2:
                                            show_notification('3 и 2 и 1', 'Добыча данных')
                                            print('line321')
                                            print(i1, i2, i3, i4, i5, i6, i7, i8)
                                            print_line((i0, i1, i2, i3, i4, i5, i6, i7, i8))
                                            # print_table(table)
                                            return line
                                        elif is2 and is1:
                                            line21 = line
                                        elif is2 and is0:
                                            line20 = line
                                        elif is1 and is0:
                                            line10 = line
                                        elif is2:
                                            line2 = line
                                        elif is1:
                                            line1 = line
                                        elif is0:
                                            line0 = line
            buffer_temp -= 1
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

    # return line21 if line21 else line20 if line20 else line10 if line10 else line2 if line2 else line1 if line1 else line0


if __name__ == '__main__':
    line = get_best_line()
    print(line)
    show_path(line)
