t = int(input())

for i in range(1, t+1):
    tmp = list(map(int, input().split()))
    print("#%d %s" %(i, max(tmp)))
