import numpy as np


primes_cache = []


def generate_primes(n):
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[0:2] = False
    for i in range(int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i*2::i] = False
    return np.where(is_prime)[0]


def divide(num: int, primes_dict: dict, divisors: dict):
    print('num: {}, divisors: {}'.format(num, divisors))
    if num in primes_dict:
        divisors.setdefault(num, 0)
        divisors[num] += 1
        return
    if num == 1:
        return

    for prime in primes_dict:
        if num % prime == 0:
            divisors.setdefault(prime, 0)
            divisors[prime] += 1

            return divide(num // prime, primes_dict, divisors)


def compile_str(divisors: dict):
    res = []
    for d in divisors:
        res.append('({}**{})'.format(d, divisors[d]) if divisors[d] > 1 else '({})'.format(d))

    return ''.join(res)


def primeFactors(n):
    global primes_cache
    if primes_cache == []:
        primes_cache = generate_primes(1000000)
    print('primes count: {}'.format(len(primes_cache)))
    print('primes [-10:] {}'.format(primes_cache[-10:]))
    primes_dict = {_: True for _ in primes_cache}
    divisors = {}
    divide(n, primes_dict, divisors)
    print('divisors: {}'.format(divisors))

    return compile_str(divisors)


if __name__ == "__main__":
    assert primeFactors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)"
