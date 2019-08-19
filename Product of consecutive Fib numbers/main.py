from itertools import count


def fast_fib_generator():
    f = [1, 1]
    yield 0
    yield 1
    yield 1
    for k in count(1):
        f.append(f[k] ** 2 + f[k - 1] ** 2)
        yield f[-1]

        f.append(f[k] * (2 * f[k + 1] - f[k]))
        yield f[-1]


def productFib(prod):
    prev_num = None
    next_num = None
    fib_gen = fast_fib_generator()
    while True:
        if prev_num is None:
            next_num = next(fib_gen)
            prev_num = next_num
            continue

        prev_num = next_num
        next_num = next(fib_gen)

        print('[{}, {}, {}]'.format(prev_num, next_num, prod))
        if prev_num * next_num == prod:
            return [prev_num, next_num, True]
        if prev_num * next_num > prod:
            return [prev_num, next_num, False]


if __name__ == "__main__":
    assert productFib(714) == [21, 34, True]
    assert productFib(800) == [34, 55, False]
    assert productFib(4895) == [55, 89, True]
    assert productFib(5895) == [89, 144, False]
