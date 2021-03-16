t = int(input())

for i in range(1, t+1):
    answer = 0
    n = int(input())
    for j in range(1, n+1):
        if j % 2 == 1: answer += j
        else: answer -= j
    print("#{} {}".format(i, answer))