from file_handler import dict_from_file
from api_handler import cache_check, write_cache

PATH = "data/currencies.txt"
URL = "https://www.cbr-xml-daily.ru/latest.js"


if cache_check(PATH) is not True:
    write_cache(PATH, URL)

currencies = dict_from_file(PATH)
BREAK_SYMBOLS = [0, " ", "0"]


def show_courses(input_data):
    column_counter = 0
    for i in currencies.items():
        column_counter += 1
        if column_counter != 4:
            print(f"{i[0]}: {round(i[1], 4)} ", end=" | ")
        else:
            print(f"{i[0]}: {round(i[1], 4)} ", end=" | \n")
            column_counter = 0
    print()


def show_hint():
    print("\nQuery format: 100 USD>RUB")


def get_value(a):
    b = a.replace(">", " ").split()
    return b


def converter(num, val1, val2):
    return abs(float(num)) / currencies[val1] * currencies[val2]


def show_result(result_data):
    result_data = get_value(result_data)
    convert_result = converter(result_data[0], result_data[1], result_data[2])
    conv = round(convert_result, 2)
    empty = '{:,}'.format(conv).replace(',', ' ')
    print(f"Result: {float(result_data[0])} {result_data[1]} = {empty} {result_data[2]}")


def main():
    show_courses(dict_from_file(PATH))
    show_hint()

    while True:
        user_input = input("Input your query: ")
        try:
            if user_input not in BREAK_SYMBOLS:
                show_result(user_input)
                show_hint()

            elif user_input in BREAK_SYMBOLS:
                break
        except:
            show_hint()
            pass


if __name__ == '__main__':
    main()

