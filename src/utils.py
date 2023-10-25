import time


def timeit(function):
    """Замерить время выполнения функции."""

    def wrapped(*args, **kwargs):
        start_time = time.perf_counter()
        res = function(*args, **kwargs)
        print(f"Время выполнение функции: {time.perf_counter() - start_time}")
        return res

    return wrapped
