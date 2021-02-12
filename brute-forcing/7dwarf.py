dwarfs = []

for _ in range(9):
    dwarfs.append(int(input()))

total = sum(dwarfs)

for i in range(8):
    for j in range(i+1, 9):
        tmp = dwarfs[i]+dwarfs[j]
        if total - tmp == 100:
            first = dwarfs[i]
            second = dwarfs[j]
            break

dwarfs.remove(first)
dwarfs.remove(second)
dwarfs.sort()

for d in dwarfs:
    print(d)