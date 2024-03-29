import json
import random
from uuid import uuid4

import uvicorn
from fastapi import FastAPI, Response
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.providers import Payment, Person

from algorithms.binary import Binary
from algorithms.brute_force import BruteForce
from entitites import Client
from utils import timeit

app = FastAPI(docs_url="/api", redoc_url=None)

DEFAULT_CLIENT_COUNT: int = 1
CLIENTS: list["Client"] = []


@app.post("/api/clients", tags=["clients"])
def generate_clients(client_count: int = DEFAULT_CLIENT_COUNT) -> None:
    """Сгенерировать список клиентов."""
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

    with open("data.json", mode="w") as file:
        json.dump(
            [
                client.model_dump(mode="json")
                for client in sorted(clients, key=lambda x: x.surname)
            ],
            file,
        )

    return None


@app.get("/api/clients", tags=["clients"])
def get_clients(client_count: int = DEFAULT_CLIENT_COUNT) -> None:
    """Получить список клиентов."""
    with open("data.json", mode="r") as file:
        clients = json.load(file)

    return [Client(**client) for client in clients[:client_count]]


@app.post("/api/clients/search", tags=["clients"])
def search_client(response: Response, surname: str) -> list[Client]:
    """Найти клиента по фамилии."""
    response.headers["Access-Control-Allow-Origin"] = "*"

    with open("data.json", mode="r") as file:
        clients = json.load(file)

    clients = [Client(**client) for client in clients]

    print()
    clients = run(clients, surname)
    print()

    return clients


@timeit
def run(clients: list[Client], surname: str) -> list[Client]:
    """Запустить алгоритм."""
    algorithm = BruteForce(clients=clients)
    for _ in range(5000):
        client = algorithm.find(surname=surname)

    return [client] if client else []


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8888, reload=True)
