def sol(arra, arrb, a, b):
    sums = []
    if a >= b:
        diff = a-b+1
        for i in range(diff):
            tmp = 0
            for j in range(b):
                tmp += arrb[j]*arra[j+i ]
            sums.append(tmp)
    if b > a:
        diff = b-a+1
        for i in range(diff):
            tmp = 0
            for j in range(a):
                tmp += arra[j]*arrb[j+i]
            sums.append(tmp)
    return max(sums)

t=int(input())
for i in range(1, t+1):
    answer = 0
    a, b = map(int, input().split())
    arra = list(map(int, input().split()))
    arrb = list(map(int, input().split()))
    answer = sol(arra, arrb, a, b)
    print("#{} {}".format(i, answer))