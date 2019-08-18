def get_prime_in_interval(start, end):
    for val in range(start, end + 1):
        if val > 1:
            for n in range(2, val // 2):
                if (val % n) == 0:
                    break
            else:
                yield val


def gap(g, m, n):
    print('g, m, n: {}, {}, {}'.format(g, m, n))
    primes_gen = get_prime_in_interval(m, n)
    prev_prime = None
    while True:
        try:
            next_prime = next(primes_gen)
        except:
            return None

        # print('next_prime: {}'.format(next_prime))
        if m <= next_prime <= n:
            # print('prev_prime: {}'.format(prev_prime))
            if prev_prime:
                # print('next_prime - prev_prime: {}'.format(next_prime - prev_prime))
                if next_prime - prev_prime == g:
                    return [prev_prime, next_prime]
            prev_prime = next_prime
        if next_prime > n:
            break

    return None


if __name__ == "__main__":
    assert gap(2, 100, 110) == [101, 103]
    assert gap(4, 100, 110) == [103, 107]
    assert gap(6, 100, 110) is None
    assert gap(8, 300, 400) == [359, 367]
    assert gap(10, 300, 400) == [337, 347]
