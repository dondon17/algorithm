t = int(input())

for i in range(1, t+1):
    tmp = list(map(int, input().split()))
    answer = 0
    for n in tmp: answer += n

    answer = round(answer / len(tmp))
    print("#%d %d" %(i, answer))

#     3
#     3 17 1 39 8 41 2 32 99 2
#     22 8 5 123 7 2 63 7 3 46
#     6 63 2 3 58 76 21 33 8 1