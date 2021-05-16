n = int(input())
k = int(input())
arr = []

for i in range(n):
    for j in range(n):
        arr.append((i+1)*(j+1))

arr.sort()
print(arr[k])