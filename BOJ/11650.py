n = int(input())
arr = []

for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x,y))


arr = sorted(arr, key=lambda x : (x[0], x[1]))

for p in arr:
    print(" ".join(map(str, p)))