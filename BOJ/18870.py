from collections import Counter

n = int(input())
numlist = list(map(int, input().split()))
numset = list(sorted(set(numlist)))

numset={numset[i]:i for i in range(len(numset))}

for e in numlist:
    print(numset[e], end=" ")
print()