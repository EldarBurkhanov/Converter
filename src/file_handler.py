def read_file(path: str) -> dict[str, float]:
    with open(path, 'r') as file:
        currencies = {key: float(value) for key, value in (line.split() for line in file.readlines())}
        return currencies

#print(read_file("data/currencies.txt"))
