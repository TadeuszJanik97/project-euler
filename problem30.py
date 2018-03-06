def digit_power_sum(n, power):
    total = 0
    while n > 0:
        total = total + pow(n % 10, power)
        n = int(n / 10)
    return total


def main():
    total = 0
    for i in range(10, 6*pow(9, 5)+1):
        if digit_power_sum(i, 5) == i:
            total += i
    print(total)


if __name__ == "__main__":
    main()
