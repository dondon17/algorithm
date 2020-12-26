
loc = input()
row = int(loc[1])
col = int(ord(loc[0]))-int(ord('a'))+1
res = 0
steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

for s in steps:
    nr=row+s[1]
    nc=col+s[0]

    if nr>=1 and nr<=8 and nc>=1 and nc<=8:
        res+=1

print(res)