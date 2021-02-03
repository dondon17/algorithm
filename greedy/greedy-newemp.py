t = int(input())

for _ in range(t):
    n = int(input())
    cnt = 1
    data = []

    for j in range(n):
        s1, s2 = map(int, input().split(" "))
        data.append((s1, s2))

    data.sort(key = lambda x:x[0])
    _min = data[0][1]

    for k in range(1, len(data)):
        if data[k][1] < _min:
            _min = data[k][1]
            cnt+=1
    print(cnt)


