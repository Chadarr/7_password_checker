import urwid

reply = urwid.Text("")


def has_digit(password: str):
    return any(letter.isdigit() for letter in password)


def is_very_long(password: str):
    return len(password) > 12


def has_letters(password: str):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password: str):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password: str):
    return any(letter.isalpha() for letter in password)


def is_symbol(letter: str):
    return not letter.isalpha() and not letter.isdigit()


def has_symbols(password: str):
    return any(is_symbol(letter) for letter in password)


def pass_rating(password: str):
    complexity_checks = [
        has_digit,
        is_very_long,
        has_letters,
        has_lower_letters,
        has_upper_letters,
        has_symbols,
    ]
    rating = 0
    for check in complexity_checks:
        rating += 2 if check(password) else 0
    return rating


def on_ask_change(edit, new_edit_text):
    reply.set_text(f"Рейтинг пароля: {pass_rating(new_edit_text)}")


def main():
    ask = urwid.Edit("Введите пароль: ", mask="*")
    menu = urwid.Pile([ask, reply])
    menu = urwid.Filler(menu, valign="top")
    urwid.connect_signal(ask, "change", on_ask_change)
    urwid.MainLoop(menu).run()


if __name__ == "__main__":
    main()
