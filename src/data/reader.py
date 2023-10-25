import csv

from entitites import Point


def read_data_from_csv() -> list[Point]:
    """Получить данные из CSV-файла."""
    data = []

    with open(
        "/Users/g.abramyan/Projects/tinkoff-workshop/src/data/data.csv", mode="r"
    ) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Пропустить заголовок

        for row in reader:
            x, y = map(float, row)
            data.append(Point(x=x, y=y))

    return data
