n = int(input())
x = list(map(int, input().split()))
x.sort()
cnt, res = 0, 0

for i in x:
    cnt += 1
    if cnt >= i:
        res += 1
        cnt = 0
    
print(res)