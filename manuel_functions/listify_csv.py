import csv


def listify_csv(filename: str) -> list:
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        data = list(reader)

    return [data[0], data[1:]]


if __name__ == "__main__":
    data_bulk = listify_csv("top10bestdnatesting.com.csv")
    print(data_bulk)
