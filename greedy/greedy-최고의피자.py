# 그리디 - 최고의 피자

tpnum = int(input())
dpri, tpri = map(int, input().split())
dcal = int(input())
tcal = []
for i in range(tpnum):
    tc = int(input())
    tcal.append(tc)
tcal.sort(reverse=True)

best = (dcal)//(dpri)
tcals = 0
for i in range(0, len(tcal)):
    for j in range(i, i+1):
        tcals += tcal[j]
    if best < (dcal+tcals)//(dpri+tpri*(i+1)):
        best = (dcal+tcals)//(dpri+tpri*(i+1))

print(best)

