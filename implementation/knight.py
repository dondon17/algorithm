loc = input().split()
x, y = int(loc[0][1]), ord(loc[0][0])-96
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]
cnt = 0

for i in range(len(dx)):
    if x + dx[i] > 0 and x + dx[i] < 9 and y + dy[i] > 0 and y + dy[i] < 9:
        cnt += 1

print(cnt)