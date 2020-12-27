def start(auto_clicker=True, alt_tab=False):
    from calculations import get_best_line, get_table, get_reqs
    table = get_table()
    reqs = get_reqs()
    line = get_best_line(table, reqs, auto_clicker)

    if auto_clicker:
        from clicker import click_on_line
        click_on_line(line, size=len(table), alt_tab=alt_tab)
    else:
        from calculations import show_path
        show_path(line)


if __name__ == '__main__':
    start(auto_clicker=True, alt_tab=True)