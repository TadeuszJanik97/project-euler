import prime_generator
import binary_search


sieve = prime_generator.generate_sieve(100000)
small_primes = prime_generator.generate(1000)
interesting_numbers = []
for number in small_primes:
    interesting_numbers.append(number)
    interesting_numbers.append((-1)*number)


def evaluate(n, a, b):
    return n*(a+n) + b


def get_sequence_length(a, b):
    i = 0
    while True:
        if sieve[evaluate(i, a, b)]:
            i = i+1
        else:
            return i


def main():
    max_chain = 0
    for a in range(-999, 1000, 2):
        for b in interesting_numbers:
            print((a, b))
            seq_len = get_sequence_length(a, b)
            if seq_len > max_chain:
                (x, y, max_chain) = (a, b, seq_len)
    print(str(x) + " " + str(y) + " " + str(max_chain))
    print(x*y)


if __name__ == '__main__':
    main()
