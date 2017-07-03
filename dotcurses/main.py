import curses


def curses_main(args):
    args = args

    window = curses.initscr()
    ch = 0
    while True:
        window.addstr(0, 0, "hej "+str(ch))

        ch = window.getch()
        if ch == ord("q"):
            break

curses.wrapper(curses_main)
