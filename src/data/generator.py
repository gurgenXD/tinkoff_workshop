import csv
import random

# Генерация 1000 случайных точек
num_points = 1000
points = [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(num_points)]

# Запись точек в CSV-файл
with open(
    "/Users/g.abramyan/Projects/tinkoff-workshop/src/data/data.csv", "w", newline=""
) as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["X", "Y"])
    for point in points:
        writer.writerow(point)

print("Файл 'data.csv' сгенерирован успешно.")
