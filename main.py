if __name__ == '__main__':
    from calculations import get_best_line, get_table, get_reqs
    table = get_table()
    reqs = get_reqs()
    line = get_best_line(table, reqs)

    # from calculations import show_path
    # show_path(line)

    from auto_clicker import click_on_line
    click_on_line(line, size=len(table))
