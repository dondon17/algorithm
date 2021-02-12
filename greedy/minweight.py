n = int(input())

weights = list(map(int, input().split()))

weights.sort()
target = 1

for i in weights:
    if target < i: 
        break
    
    target += i

print(target)