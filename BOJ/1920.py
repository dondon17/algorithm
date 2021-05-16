n = int(input())
numbers = list(map(int, input().split()))

m = int(input())
search = list(map(int, input().split()))

for e in search:
    if e in numbers: print(1)
    else: print(0)