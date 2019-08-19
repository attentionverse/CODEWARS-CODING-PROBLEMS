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
    def stream():
        index = 0
        if not Primes.cache:
            Primes.sieve_primes(16000000)
        while True:
            yield Primes.cache[index]
            index += 1


if __name__ == "__main__":
    # start = time.time()
    #
    # stream = Primes.stream()
    # for i in range(1000000):
    #     next_prime = next(stream)
    #     if i % 50000 == 0:
    #         end = time.time()
    #         print('{}: {} – {}'.format(end - start, i, next_prime))
    #
    # end = time.time()
    # print('{}: {}'.format(end - start, next_prime))

    def verify(from_n, *vals):
        stream = Primes.stream()
        for _ in range(from_n):
            next(stream)
        for v in vals:
            assert next(stream) == v

    verify(0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    verify(10, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    verify(100, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601)
    verify(1000, 7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017)
