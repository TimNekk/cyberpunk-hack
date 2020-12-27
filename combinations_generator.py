def get_lines_4(size):
    lines = []
    i0 = 0
    for i1 in range(size):
        buffer_temp = 4
        while buffer_temp != 0:
            for i2 in range(size):
                if i2 == i0:
                    continue

                for i3 in range(size):
                    if i3 == i1:
                        continue

                    for i4 in range(size):
                        i_all = ((i1, i0), (i1, i2), (i3, i2), (i3, i4))

                        if i4 == i2 or len(i_all) != len(set(i_all)):
                            continue

                        line = [i0, i1, i2, i3, i4]

                        lines.append(line)
            buffer_temp -= 1
    return lines


def get_lines_5(size):
    lines = []
    i0 = 0
    for i1 in range(size):
        buffer_temp = 5
        while buffer_temp != 0:
            for i2 in range(size):
                if i2 == i0:
                    continue

                for i3 in range(size):
                    if i3 == i1:
                        continue

                    for i4 in range(size):
                        if i4 == i2:
                            continue

                        for i5 in range(size):
                            i_all = ((i1, i0), (i1, i2), (i3, i2), (i3, i4), (i5, i4))

                            if i5 == i3 or len(i_all) != len(set(i_all)):
                                continue

                            line = [i0, i1, i2, i3, i4, i5]

                            lines.append(line)
            buffer_temp -= 1
    return lines


def get_lines_6(size):
    lines = []
    i0 = 0
    for i1 in range(size):
        buffer_temp = 6
        while buffer_temp != 0:
            for i2 in range(size):
                if i2 == i0:
                    continue

                for i3 in range(size):
                    if i3 == i1:
                        continue

                    for i4 in range(size):
                        if i4 == i2:
                            continue

                        for i5 in range(size):
                            if i5 == i3:
                                continue

                            for i6 in range(size):
                                i_all = ((i1, i0), (i1, i2), (i3, i2), (i3, i4), (i5, i4), (i5, i6))

                                if i6 == i4 or len(i_all) != len(set(i_all)):
                                    continue

                                line = [i0, i1, i2, i3, i4, i5, i6]

                                lines.append(line)
            buffer_temp -= 1
    return lines


def get_lines_7(size):
    lines = []
    i0 = 0
    for i1 in range(size):
        buffer_temp = 7
        while buffer_temp != 0:
            for i2 in range(size):
                if i2 == i0:
                    continue

                for i3 in range(size):
                    if i3 == i1:
                        continue

                    for i4 in range(size):
                        if i4 == i2:
                            continue

                        for i5 in range(size):
                            if i5 == i3:
                                continue

                            for i6 in range(size):
                                if i6 == i4:
                                    continue

                                for i7 in range(size):
                                    i_all = ((i1, i0), (i1, i2), (i3, i2), (i3, i4), (i5, i4), (i5, i6), (i7, i6))

                                    if i7 == i5 or len(i_all) != len(set(i_all)):
                                        continue

                                    line = [i0, i1, i2, i3, i4, i5, i6, i7]

                                    lines.append(line)
            buffer_temp -= 1
    return lines


def get_lines_8(size):
    lines = []
    i0 = 0
    for i1 in range(size):
        buffer_temp = 8
        while buffer_temp != 0:
            for i2 in range(size):
                if i2 == i0:
                    continue

                for i3 in range(size):
                    if i3 == i1:
                        continue

                    for i4 in range(size):
                        if i4 == i2:
                            continue

                        for i5 in range(size):
                            if i5 == i3:
                                continue

                            for i6 in range(size):
                                if i6 == i4:
                                    continue

                                for i7 in range(size):
                                    if i7 == i5:
                                        continue

                                    for i8 in range(size):
                                        i_all = (
                                            (i1, i0), (i1, i2), (i3, i2), (i3, i4), (i5, i4), (i5, i6), (i7, i6),
                                            (i7, i8))

                                        if i8 == i6 or len(i_all) != len(set(i_all)):
                                            continue

                                        line = [i0, i1, i2, i3, i4, i5, i6, i7, i8]

                                        lines.append(line)
            buffer_temp -= 1
    return lines


def get_lines(buffer, size):
    return get_lines_4(size) if buffer == 4 else get_lines_5(size) if buffer == 5 else get_lines_6(size) if buffer == 6 else \
                get_lines_7(size) if buffer == 7 else get_lines_8(size) if buffer == 8 else False


if __name__ == '__main__':
    print(get_lines_8(6)[0])
