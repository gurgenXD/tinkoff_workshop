import uvicorn
from fastapi import FastAPI

from algorithms.branch_and_bound import BranchAndBound
from algorithms.brute_force import BruteForce
from data.reader import read_data_from_csv
from entitites import Point

app = FastAPI(docs_url="/api", redoc_url=None)


@app.get("/api/points", tags=["points"])
def get_points() -> list[Point]:
    """Получить список координат."""
    return read_data_from_csv()


@app.post("/api/points/shortest-path", tags=["points"])
def find_shortest_path(points: list[Point]) -> list[Point]:
    """Найти кратчайший путь."""
    print()

    # shortest_path, min_distance = BruteForce(points=points).find()
    shortest_path, min_distance = BranchAndBound(points=points).find()

    print(f"Кратчайшее расстояние: {min_distance}")
    print()

    return shortest_path


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)
