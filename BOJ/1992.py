import sys

n = int(sys.stdin.readline())
tree = [list(sys.stdin.readline().strip()) for _ in range(n)]

def quadTree(x, y, n):

    if n == 1:
        print(tree[x][y], end="")
        return

    base = tree[x][y]
    flag = True
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tree[i][j] != base:
                flag = False
                break
    if flag:
        print(base, end="")
    else:
        print("(", end="")
        quadTree(x, y, n//2)
        quadTree(x, y+n//2, n//2)
        quadTree(x+n//2, y, n//2)
        quadTree(x+n//2, y+n//2, n//2)
        print(")", end="")

quadTree(0, 0, n)
print()