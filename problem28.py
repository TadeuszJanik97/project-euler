element = 1
total = 1
lvl = 1
jump = 2

while lvl <= 500:
    for i in range(0, 4):
        element = element + jump
        total = total + element
    lvl = lvl + 1
    jump = jump + 2

print(total)
