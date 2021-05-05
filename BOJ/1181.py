n = int(input())
arr = []

for _ in range(n):
    word = input()
    if word in arr:
        continue
    arr.append(word)


arr = sorted(arr, key=lambda x : (len(x), x))

for p in arr:
    print(p)