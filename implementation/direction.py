x, y = 1, 1
_dir = ["L", "R", "U", "D"]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(input())
route = input().split()

for _route in route:
    for i in range(len(_dir)):
        if _route == _dir[i]:
            if x+dx[i] < 1 or y+dy[i] < 1 or x+dx[i] > n or y+dy[i] > n: 
                continue
            else:
                x += dx[i]
                y += dy[i]

print(x,y)