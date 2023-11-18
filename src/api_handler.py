import urllib.request
import json


def get_json(link: str) -> dict[str, float]:
    with urllib.request.urlopen(link) as url:
        data = json.load(url)
    return data["rates"]


def write_currencies(currencies: dict[str, float], path: str) -> None:
    with open(path, "a") as file:
        for key, value in currencies.items():
            file.write("{} {}\n".format(key, value))

        file.write("RUB 1.00")


def cache_check(path: str) -> bool:
    try:
        with open(path, "r") as file:
            temp = file.read()
            return True
    except:
        return False

#write_currencies(get_json("https://www.cbr-xml-daily.ru/latest.js"), "data/currencies.txt")
#print(cache_check("data/currencies.txt"))