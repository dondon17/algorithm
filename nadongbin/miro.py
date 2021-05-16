import sys 
from collections import deque

r, c = map(int, sys.stdin.readline().split())
miro = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(r):
    miro.append(list(map(int, input())))

queue = deque()
queue.append((0, 0))

while queue:
    x, y = queue.popleft()
    if miro[x][y] == 1:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= r or ny >= c:
                continue
            if miro[nx][ny] == 0:
                continue
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx,ny))

print(miro[x-1][y-1])