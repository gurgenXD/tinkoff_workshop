from uuid import UUID

from mimesis.enums import Gender
from pydantic import BaseModel


class Client(BaseModel):
    """Клиент."""

    id: UUID
    name: str
    surname: str
    gender: Gender
    email: str
    phone: str
    age: int
    credit_card_number: str
    credit_card_expiration_date: str
