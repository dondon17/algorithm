def sol(arra, arrb, a, b):
    _short = a if a<b else b
    _long = a if a>b else b
    d = _long-_short
    for i in range(d+1):
        tmp = 0
        _max = -10000000
        for j in range(_short):
            tmp += arra[j]*arrb[j+i]
        _max = tmp if tmp >= _max else _max
            
    return _max

    
t=int(input())
for i in range(1, t+1):
    answer = 0
    a, b = map(int, input().split())
    arra = list(map(int, input().split()))
    arrb = list(map(int, input().split()))
    answer = sol(arra, arrb, a, b)
    print("#{} {}".format(i, answer))