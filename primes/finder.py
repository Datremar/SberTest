import getopt
import sys

from itertools import count


def primes():
    yield 2

    primes_cashed = [2]

    for num in count(3, 2):
        is_prime = True

        for prime in primes_cashed:
            if num % prime == 0:
                is_prime = False
                break

        if is_prime:
            primes_cashed.append(num)
            yield num


def main(options):
    n = 10000
    for name, value in options:
        if name in ['-n', '--number']:
            n = value

    k = 0
    for prime in primes():
        k += 1
        if k == n:
            print(prime)
            break


if __name__ == '__main__':
    options, _ = getopt.getopt(sys.argv, "n:", ["number ="])
    main(options)
