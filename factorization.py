import prime_generator as g
import math


def factorize(n):
    factors = g.generate(math.floor(n))
    d = {}
    for f in factors:
        d[f] = 0
    while n > 1:
        for f in factors:
            if n % f == 0:
                d[f] = d[f] + 1
                n = n/f
                break
    result = {}
    for k in d.keys():
        if d[k] != 0:
            result[k] = d[k]
    return result


def power(factorization, n):
    result = dict(factorization)
    for k in result.keys():
        result[k] = n*result[k]
    return result


def to_string(factorization):
    result = ""
    for k in sorted(factorization.keys()):
        result = result + str(k) + " " + str(factorization[k]) + " "
    return result
