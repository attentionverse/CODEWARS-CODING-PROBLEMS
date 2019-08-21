cache = {}


def fibonacci(n):
    global cache

    if n in [0, 1]:
        return n
    if n in cache:
        return cache[n]

    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return cache[n]


if __name__ == "__main__":
    assert fibonacci(70) == 190392490709135
    assert fibonacci(60) == 1548008755920
    assert fibonacci(50) == 12586269025
