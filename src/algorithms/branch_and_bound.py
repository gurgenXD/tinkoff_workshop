import itertools
import math
from dataclasses import dataclass
from typing import TYPE_CHECKING

from utils import timeit

if TYPE_CHECKING:
    from entitites import Point


@dataclass
class BranchAndBound:
    """Алгоритм ветвей и границ."""

    points: list["Point"]

    @timeit
    def find(self) -> tuple[list["Point"] | None, float]:
        """Нахождение кратчайшего обхода всех точек через метод ветвей и границ."""
        starting_point = self.points[0]
        min_path: list["Point"] | None = None
        min_distance = float("inf")

        for permutation in itertools.permutations(range(1, len(self.points))):
            current_path = [starting_point] + [self.points[i] for i in permutation]
            current_distance = self.calc_total_distance(current_path)

            if current_distance < min_distance:
                min_distance = current_distance
                min_path = current_path

        return min_path, min_distance

    def calc_total_distance(self, path: list["Point"]) -> float:
        """Рассчитать дистанцию."""
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += self.calc_distance(path[i], path[i + 1])

        # Учитываем расстояние между последней и первой точками.
        total_distance += self.calc_distance(path[-1], path[0])

        return total_distance

    @staticmethod
    def calc_distance(point1: "Point", point2: "Point") -> float:
        """Вычисление расстояния между двумя точками."""
        return math.sqrt((point2.x - point1.y) ** 2 + (point2.x - point1.y) ** 2)
