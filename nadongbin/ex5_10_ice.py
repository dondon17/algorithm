r, c = map(int, input().split())
pan = []
for _ in range(r):
    pan.append(list(map(int, input())))

def dfs(x, y):
    global pan, r, c
    if x < 0 or x >= r or y < 0 or y >= c:
        return False
    
    if pan[x][y] == 0:
        pan[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    
    return False

answer = 0
for i in range(r):
    for j in range(c):
        if dfs(i, j):
            answer += 1

print(answer)