import numpy as np


def generate_primes(n):
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[0:2] = False
    for i in range(int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i*2::i]=False
    return np.where(is_prime)[0]


def get_prime_in_interval(start, end):
    primes = generate_primes(end)
    for prime in primes:
        if prime >= start:
            yield prime


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
