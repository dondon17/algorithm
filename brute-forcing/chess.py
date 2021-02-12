n, m = map(int, input().split())
board = []
fix = []

for _ in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7):
        firstw = 0
        firstb = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if board[k][l] != 'W':
                        firstw += 1
                    if board[k][l] != 'B':
                        firstb += 1
                        
                else:
                    if board[k][l] != 'W':
                        firstb += 1
                    if board[k][l] != 'B':
                        firstw += 1
        fix.append(firstw)
        fix.append(firstb)

print(min(fix))