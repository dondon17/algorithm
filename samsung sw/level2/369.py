arr = ["3", "6", "9"]

n = int(input())

for i in range(1, n+1):
    cnt = 0
    for j in str(i):
        if j in arr: cnt += 1
        else: continue
    if cnt == 0: 
        print(i, end=" ")
    else: 
        print("-"*cnt, end=" ")