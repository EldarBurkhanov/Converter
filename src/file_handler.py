def dict_from_file(path):
    currensies = {}
    with open(path, "r") as file:
        text = file.readlines()
        for i in text:
            key, value = i.split()
            currensies[key] = float(value)

    return currensies



