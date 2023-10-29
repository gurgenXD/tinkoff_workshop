from dataclasses import dataclass
from typing import TYPE_CHECKING

from utils import timeit

if TYPE_CHECKING:
    from entitites import Client


@dataclass
class BruteForce:
    """Алгоритм "грубой силы"."""

    clients: list["Client"]

    @timeit
    def find(self, surname: str) -> "Client | None":
        """Нахождение пользователя по фамилии."""
        for client in self.clients:
            if client.surname == surname:
                return client

        return None
