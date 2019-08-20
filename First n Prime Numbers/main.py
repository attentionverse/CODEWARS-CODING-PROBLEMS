import math
import numpy
import time


class Primes:
    cache = []

    @staticmethod
    def sieve_primes(n):
        sieve = numpy.ones(n // 2, dtype=numpy.bool)
        limit = int(math.sqrt(n)) + 1

        for i in range(3, limit, 2):
            if sieve[i // 2]:
                sieve[i * i // 2:: i] = False

        prime_indexes = numpy.nonzero(sieve)[0][1::]
        primes = 2 * prime_indexes.astype(numpy.int32) + 1

        Primes.cache.append(2)
        Primes.cache.extend(primes)

    @staticmethod
    def first(n):
        if not Primes.cache:
            Primes.sieve_primes(370000)
        if n == 1:
            return [Primes.cache[0]]
        return Primes.cache[0:n]


if __name__ == "__main__":
    assert Primes.first(1) == [2]
    assert Primes.first(2) == [2, 3]
    assert Primes.first(5) == [2, 3, 5, 7, 11]
    assert Primes.first(20)[-5:] == [53, 59, 61, 67, 71]
    assert Primes.first(100)[99] == 541
    assert Primes.first(80)[79] == 409
