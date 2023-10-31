from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entitites import Client


@dataclass
class Binary:
    """Бинарный поиск."""

    clients: list["Client"]

    def find(self, surname: str) -> "Client | None":
        """Нахождение пользователя по фамилии."""
        left, right = 0, len(self.clients) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_client = self.clients[mid]

            if mid_client.surname == surname:
                return mid_client
            elif mid_client.surname < surname:
                left = mid + 1
            else:
                right = mid - 1

        return None
