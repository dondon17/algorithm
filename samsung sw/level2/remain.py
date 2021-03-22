def solution(c):
    cnt = [0]*8
    if c % 10 != 0: 
        c -= c%10
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    while c>0:
        for i in range(len(money)):
            cnt[i] += c // money[i]
            c -= cnt[i]*money[i]

    return cnt

t = int(input())
for i in range(1, t+1):
    answer = []
    cash = int(input())
    print("#{}".format(i))
    answer = solution(cash)
    print(*answer, sep = " ")
