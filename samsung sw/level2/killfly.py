t = int(input())

for i in range(1, t+1):
    answer = -1
    _map = []
    n, m = map(int, input().split())

    for j in range(n):
        _map.append(list(map(int, input().split())))

    for k in range(n-m+1):
        for l in range(n-m+1):
            tmp = 0
            for o in range(k, k+m):
                for p in range(l, l+m):
                    tmp += _map[o][p]
            answer = tmp if tmp >= answer else answer
    
    print("#%d %d" %(i, answer))