def generate(n):
    a = []
    for i in range(2, n+1):
        a.append(True)
    p = 2
    primes = []
    while p**2 <= n:
        j = p**2
        while j <= n:
            a[j-2] = False
            j = j+p
        p = p + 1
        while not a[p-2]:
            p = p+1
    for i in range(2, n+1):
        if a[i-2]:
            primes.append(i)
    return primes
