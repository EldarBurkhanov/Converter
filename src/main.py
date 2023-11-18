from api_handler import *
from file_handler import *

PATH = "data/currencies.txt"
URL = "https://www.cbr-xml-daily.ru/latest.js"
BREAK_SYMBOLS = [0, " ", "0"]


def show_currencies(cur_list: dict) -> None:
    column_counter = 0
    for i in cur_list.items():
        column_counter += 1
        if column_counter != 4:
            print(f"{i[0]}: {round(i[1], 4)} ".ljust(15, " "), end="| ")
        else:
            print(f"{i[0]}: {round(i[1], 4)} ".ljust(15, " "), end="| \n")
            column_counter = 0


def show_hint() -> None:
    print("\nQuery format: 100 USD>RUB")


def get_value(a: str) -> list:
    """Convert user input to command list
    Example: str: "100 USD>UZS" -> list[100, "USD", "UZS"]
    :param a:
    :return:
    """
    b = a.replace(">", " ").split()
    return b


def converter(num: float, val1: str, val2: str, cur_list: dict) -> float:
    return float(num) / cur_list[val1] * cur_list[val2]


def show_result(user_input: str, cur_list: dict[str, float]) -> None:
    temp = get_value(user_input)
    conver_result = round(converter(temp[0], temp[1], temp[2], cur_list), 2)
    print(f"Result: "
          f"{float(temp[0])} "
          f"{temp[1]} = {'{:,}'.format(conver_result).replace(',', ' ')} "
          f"{temp[2]}")


def main() -> None:
    if not cache_check(PATH):
        # print("Cache was taken from URL")
        write_currencies(get_json(URL), PATH)
        empty = get_json(URL)
    else:
        # print("Cache was taken from File")
        empty = read_file(PATH)

    show_currencies(empty)
    show_hint()

    while True:
        user_input = input("Input your query: ")
        try:
            if user_input not in BREAK_SYMBOLS:
                show_result(user_input, empty)
                show_hint()
            elif user_input in BREAK_SYMBOLS:
                break
        except:
            show_hint()

    # print(get_value(user_input))
    # print(converter(500, "USD", "UZS", empty))


if __name__ == '__main__':
    main()
