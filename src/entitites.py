from pydantic import BaseModel


class Point(BaseModel):
    """Схема точки."""

    x: float
    y: float
