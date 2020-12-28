arr = input().split('-')
res = 0

for i in arr[0].split('+'):
    res += int(i)

for i in arr[1:]:
    tmp = 0
    for j in i.split('+'):
        tmp += int(j)
    res -= tmp

print(res)
