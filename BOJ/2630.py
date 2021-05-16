import sys
myinput = sys.stdin.readline

n = int(myinput())
tree = [list(map(int, myinput().split())) for _ in range(n)]
cnt = [0, 0]

def quadTree(y, x, n):
    base = tree[y][x]
    flag = True

    for row in range(y, y+n):
        for col in range(x, x+n):
            if tree[row][col] != base:
                quadTree(y, x, n//2)
                quadTree(y+n//2, x, n//2)
                quadTree(y, x+n//2, n//2)
                quadTree(y+n//2, x+n//2, n//2)
                return
    cnt[base] += 1

quadTree(0, 0, n)
for e in cnt:
    print(e)
