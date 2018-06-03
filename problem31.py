ret = 0

for p1 in range(0, 201):
    total = p1
    for p2 in range(0, (200 - total) // 2 + 1):
        total += 2 * p2
        for p5 in range(0, (200 - total) // 5 + 1):
            total += 5 * p5
            for p10 in range(0, (200 - total) // 10 + 1):
                total += 10 * p10
                for p20 in range(0, (200 - total) // 20 + 1):
                    total += 20 * p20
                    for p50 in range(0, (200 - total) // 50 + 1):
                        total += 50 * p50
                        for p100 in range(0, (200 - total) // 100 + 1):
                            total += 100 * p100
                            for p200 in range(0, (200 - total) // 200 + 1):
                                total += 200 * p200
                                if total == 200:
                                    ret += 1
                            total = p1 + 2 * p2 + 5 * p5 + 10 * p10 + 20 * p20 + 50 * p50
                        total = p1 + 2 * p2 + 5 * p5 + 10 * p10 + 20 * p20
                    total = p1 + 2 * p2 + 5 * p5 + 10 * p10
                total = p1 + 2 * p2 + 5 * p5
            total = p1 + 2 * p2
        total = p1

print(ret)
