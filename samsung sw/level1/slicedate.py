t = int(input())
day31 = [1,3,5,7,8,10,12]
day30 = [4,6,9,11]
day28 = [2]

def sol(ymd):
    if len(ymd) != 8: return "-1"

    _year = int(ymd[:4])
    _month = int(ymd[4:6])
    _day = int(ymd[6:])

    if _month < 1 or _month > 12: return "-1"
    if _month in day31 and (_day>31 or _day<1): return "-1"
    if _month in day30 and (_day>30 or _day<1): return "-1"
    if _month in day28 and (_day>28 or _day<1): return "-1"

    return ymd[:4]+"/"+ymd[4:6]+"/"+ymd[6:]

for i in range(1, t+1):
    ymd = input()
    answer = sol(ymd)
    print("#%d %s" %(i, answer))