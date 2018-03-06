import factorization as f

s = set()

for i in range(2, 101):
    factors = f.factorize(i)
    for j in range(2, 101):
        s.add(f.to_string(f.power(factors, j)))

print(s)
print(len(s))
