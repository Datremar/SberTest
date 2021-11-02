from triangles import three_alike, gen_triangles
from primes import get_primes


def has_prime(v: tuple, primes):
    if v[1] in primes or v[2] in primes:
        return True

    return False


s = int(input())

vs = []

for a in range(2, s, 2):
    for b in range(a + 1, s):
        for d in range(a + 1, s):
            if d + b >= s:
                break

            if three_alike(*gen_triangles(a, b, d)):
                vs.append((a, b, d))

for variant in vs:
    print(variant)

print(len(vs))
