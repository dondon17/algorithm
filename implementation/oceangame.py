n, m = map(int, input().split())
x, y, _dir = map(int, input().split())
check = [[0]*m for _ in range(n)] # 0으로 채워진 n * m 행렬 생성
check[x][y] = 1 # 시작 위치 방문 처리

_map = []
for i in range(n):
    _map.append(list(map(int, input().split())))

count = 1
turn_time = 0 # 4방이 이미 방문한 곳이거나 바다인 경우를 체크하기 위함

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turnleft():
    global _dir
    _dir -= 1
    if _dir == -1:
        _dir = 3

while True:
    turnleft()
    nx = x + dx[_dir]
    ny = y + dy[_dir]

    if check[nx][ny] == 0 and _map[nx][ny] == 0:
        check[nx][ny] = 1
        x, y = nx, ny
        count += 1 
        turn_time = 0
        continue
    else:
        turn_time+=1

    if turn_time == 4:
        nx = x-dx[_dir]
        ny = y-dy[_dir]
        if _map[nx][ny] == 0:
            x, y = nx, ny
        else: break
        turn_time = 0

print(count)