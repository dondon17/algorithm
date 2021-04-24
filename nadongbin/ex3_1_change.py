changes = [500, 100, 50, 10]
answer = 0

N = int(input())

for change in changes:
    answer += N//change
    N%=change

print(answer)