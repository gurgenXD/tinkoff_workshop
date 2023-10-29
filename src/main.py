import random
from uuid import uuid4

import uvicorn
from fastapi import FastAPI
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.providers import Payment, Person

from algorithms.binary import Binary
from algorithms.brute_force import BruteForce
from entitites import Client

app = FastAPI(docs_url="/api", redoc_url=None)

DEFAULT_CLIENT_COUNT: int = 1
CLIENTS: list["Client"] = []


@app.get("/api/clients", tags=["clients"])
def get_clients(client_count: int = DEFAULT_CLIENT_COUNT) -> list[Client]:
    """Получить список клиентов."""
    person = Person(locale=Locale.RU)
    payment = Payment()

    clients: list["Client"] = []
    for _ in range(client_count):
        gender = random.choice(list(Gender))

        clients.append(
            Client(
                id=uuid4(),
                name=person.name(gender=gender),
                surname=person.surname(gender=gender),
                gender=gender,
                email=person.email(),
                phone=person.phone_number(),
                age=person.age(),
                credit_card_number=payment.credit_card_number(),
                credit_card_expiration_date=payment.credit_card_expiration_date(),
            )
        )

    global CLIENTS
    CLIENTS = sorted(clients, key=lambda x: x.surname)

    return CLIENTS[-2:-1]


@app.post("/api/clients/find", tags=["clients"])
def find_client(surname: str) -> Client | None:
    """Найти клиента по фамилии."""

    print()
    print("Поиск 'Грубой силой'.")
    algorithm = BruteForce(clients=CLIENTS)
    client = algorithm.find(surname=surname)

    print()
    print("Бинарный поиск")
    algorithm = Binary(clients=CLIENTS)
    client = algorithm.find(surname=surname)
    print()

    return client


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8888, reload=True)
