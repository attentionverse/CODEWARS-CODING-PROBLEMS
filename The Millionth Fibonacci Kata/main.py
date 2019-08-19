import math


cache = {}
fn = []


def fill_neg(n):
    global fn

    # fill negative
    a, b = 0, 1
    fn.append(a)
    for i in range(0, n+1):
        a, b = b - a, a
        fn.append(a)


def fast_fib(n):
    global cache

    if n == 0:
        return 0
    elif n <= 2:
        return 1

    if n in cache:
        return cache[n]

    k = n // 2
    a = fast_fib(k)
    b = fast_fib(k + 1)

    if n % 2:
        cache[n] = a * a + b * b
    else:
        cache[n] = a * (2 * b - a)

    return cache[n]


def fib(n):
    print('n: {}'.format(n))

    if n < 0 and not fn:
        fill_neg(100)

    if n >= 0:
        f = fast_fib(n)
        print('f: {}'.format(f))
        return f
    else:
        return fn[n*-1]


if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(-6) == -8
    assert fib(-96) == -51680708854858323072
    assert fib(-37) == 24157817
    assert fib(-94) == -19740274219868223167
    assert fib(-79) == 14472334024676221
    assert fib(-59) == 956722026041
    assert fib(-69) == 117669030460994
    assert fib(-26) == -121393
    assert fib(-48) == -4807526976
    assert fib(-28) == -317811
    assert fib(-91) == 4660046610375530309


    fib_1000 = fib(1000)
    fib_1001 = fib(1001)

    print(fib_1001 / fib_1000)
    print((1 + math.sqrt(5)) / 2)
