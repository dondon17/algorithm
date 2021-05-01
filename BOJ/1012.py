dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(x, y):
    stack = [(x, y)]

    for d in dirs:
        nx = x + d[0]
        ny = y + d[1]
        if nx >= 0 and nx < n and ny >= 0 and ny < m and baechu[nx][ny] == 1:
            stack.append((nx, ny))
            baechu[x][y] = 0
        else:
            stack.pop()


testcase = int(input())
for i in range(testcase):
    m, n, k = map(int, input().split())
    baechu = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        baechu[y][x] = 1

    result = 0 
    for r in range(n):
        for c in range(m):
            if baechu[r][c] == 1:
                result += 1
    
    print(result)

