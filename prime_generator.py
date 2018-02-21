def generate(n):
    primes = []
    a = generate_sieve(n)
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
    return primes


def generate_sieve(n):
    a = [False, False]
    for i in range(2, n + 1):
        a.append(True)
    p = 2
    while p ** 2 <= n:
        j = p ** 2
        while j <= n:
            a[j] = False
            j = j + p
        p = p + 1
        while not a[p]:
            p = p + 1
    return a
