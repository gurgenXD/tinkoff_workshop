import itertools
import math
from dataclasses import dataclass
from typing import TYPE_CHECKING

from utils import timeit

if TYPE_CHECKING:
    from entitites import Point


@dataclass
class BruteForce:
    """Алгоритм "грубой силы"."""

    points: list["Point"]

    @timeit
    def find(self) -> tuple[list["Point"] | None, float]:
        """Нахождение кратчайшего обхода всех точек через метод "грубой силы"."""
        min_distance = float("inf")
        best_path: list["Point"] | None = None

        for permutation in itertools.permutations(self.points):
            total_distance = 0
            for i in range(len(permutation) - 1):
                total_distance += self.calc_distance(permutation[i], permutation[i + 1])

            # Учитываем расстояние между последней и первой точками.
            total_distance += self.calc_distance(permutation[-1], permutation[0])

            if total_distance < min_distance:
                min_distance = total_distance
                best_path = permutation

        return best_path, min_distance

    @staticmethod
    def calc_distance(point1: "Point", point2: "Point") -> float:
        """Вычисление расстояния между двумя точками."""
        return math.sqrt((point2.x - point1.y) ** 2 + (point2.x - point1.y) ** 2)
