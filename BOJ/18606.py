import sys
r = sys.stdin.readline

t = int(r().strip())

for _ in range(t):
    n, m, q = map(int, r().split())
    frame = [[1]*n for _ in range(m)]

    for _ in range(q):
        cnt = 0
        i, j = map(int, r().split())
        frame[i][j] = 0
        

