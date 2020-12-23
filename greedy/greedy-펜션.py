# 그리디 - 펜션
n, m = map(int, input().split())
room = []

for i in range(n):
    room.append(input())

s, t = map(int, input().split())

for j in range(0, m):
    if roomstate[s-1][j] == 'O':
        marking.append(j)



