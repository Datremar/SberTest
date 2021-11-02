def is_prime(num):
    if num % 2 == 0:
        return False

    for i in range(3, num, 2):
        if num % i == 0:
            return False

    return True


def get_primes(lim=1000):
    primes = []
    for num in range(2, lim):
        if is_prime(num):
            primes.append(num)

    return primes

