from collections import Counter

n = int(input())
numbers = list(map(int, input().split()))
counter = Counter(numbers)

m = int(input())
search = list(map(int, input().split()))


for e in search:
    print(counter[e], end=" ")
print()