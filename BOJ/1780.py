import sys
myinput = sys.stdin.readline

n = int(myinput())
tree = [list(map(int, myinput().split())) for _ in range(n)]
cnt = [0, 0, 0]
answer= []

def quadTree(y, x, n):
    base = tree[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if tree[i][j] != base:
                quadTree(y, x, n//3)
                quadTree(y+n//3, x, n//3)
                quadTree(y+2*(n//3), x, n//3)
                quadTree(y, x+n//3, n//3)
                quadTree(y, x+2*(n//3), n//3)
                quadTree(y+n//3, x+n//3, n//3)
                quadTree(y+n//3, x+2*(n//3), n//3)
                quadTree(y+2*(n//3), x+n//3, n//3)
                quadTree(y+2*(n//3), x+2*(n//3), n//3)
                return
    answer.append(base)
    cnt[base+1] += 1

quadTree(0, 0, n)
for e in cnt:
    print(e)

