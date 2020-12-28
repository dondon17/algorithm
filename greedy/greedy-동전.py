n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

cnt = 0
for money in arr:
    if money <= m:
        cnt += m//money
        m %= money

print(cnt)

