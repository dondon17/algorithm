import sys
myinput = sys.stdin.readline

n, m = map(int, myinput().split())
A = [list(map(int, myinput().split())) for _ in range(n)]

r, k = map(int, myinput().split())
B= [list(map(int, myinput().split())) for _ in range(r)]

for row in A:
    for a in row:
        for j in range(k):
            for i in range(r):
                print("a : {}, b: {}".format(a, B[i][j])) 
