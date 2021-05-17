import sys
myinput = sys.stdin.readline

n, m = map(int, myinput().split())
A = [list(map(int, myinput().split())) for _ in range(n)]

r, c = map(int, myinput().split())
B= [list(map(int, myinput().split())) for _ in range(r)]

AB = []

for i in range(len(A)):
    tmpArr = []
    for j in range(len(B[0])):
        tmp = 0
        for k in range(len(A[0])):
            tmp += A[i][k]*B[k][j]
        tmpArr.append(tmp)
    AB.append(tmpArr)

for row in AB:
    for e in row:
        print(e, end=" ")
    print()