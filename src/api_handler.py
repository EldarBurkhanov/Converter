import urllib.request
import json

def get_json(link):
    currensies = {}
    with urllib.request.urlopen(link) as url:
        data = json.load(url)
        for key, value in data["rates"].items():
            currensies[key] = float(value)

    return currensies


def cache_check(path):
    with open(path, 'r') as file:
        return True if len(file.read()) > 1 else False


def write_cache(path, link):
    with open(path, 'w') as file:
        get_data = get_json(link)
        for key, value in get_data.items():
            file.write(f"{key} {value}\n")
