import curses


def main_menu(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    options = ["Criar Lead", "Placeholder 1",
               "Placeholder 2", "Placeholder 3", "Sair"]
    selected = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, "Selecione uma opção:", curses.A_BOLD)

        for i, option in enumerate(options):
            if i == selected:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(i + 2, 4, f"> {option} <")
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(i + 2, 6, option)

        key = stdscr.getch()

        if key in [curses.KEY_UP, ord('w')]:
            selected = (selected - 1) % len(options)
        elif key in [curses.KEY_DOWN, ord('s')]:
            selected = (selected + 1) % len(options)
        elif key in [ord(str(i + 1)) for i in range(len(options))]:
            selected = int(chr(key)) - 1
        elif key in [curses.KEY_ENTER, 10, 13]:
            if selected == len(options) - 1:
                break  # Exit on "Sair"
            return selected

    return None


def main():
    selected_option = curses.wrapper(main_menu)
    if selected_option is not None:
        print(f"Opção selecionada: {selected_option + 1}")
        if selected_option == 0:
            print("Executando Criar Lead...")
            # Chamar função de criar lead aqui
        else:
            print("Função Placeholder ainda não implementada.")


if __name__ == "__main__":
    main()
