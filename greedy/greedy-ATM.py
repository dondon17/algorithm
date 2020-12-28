n = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum = 0
for i in range(0, len(arr)):
    for j in range(0, i+1):
        sum += arr[j]

print(sum)