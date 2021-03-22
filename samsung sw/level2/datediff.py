def sol(m1, d1, m2, d2):
    day31 = [1,3,5,7,8,10,12]
    day30 = [4,6,9,11]
    day28 = [2]

    day1, day2 = 0, 0
    for i in range(1, m1):
        if i in day31: day1 += 31
        elif i in day30: day1 += 30
        else: day1 += 28
    day1 += d1
    for i in range(1, m2):
        if i in day31: day2 += 31
        elif i in day30: day2 += 30
        else: day2 += 28
    day2 += d2
    
    return day2-day1+1

t = int(input())

for i in range(1, t+1):
    answer = 0
    m1, d1, m2, d2 = map(int, input().split())
    answer = sol(m1, d1, m2, d2)
    print("#{} {}".format(i, answer))