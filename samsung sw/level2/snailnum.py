def sol(num):
    cnt = 1
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    arr = [[0]*num]*num
    print(arr)
    for i in range(num):
        for j in range(num):
            

t = int(input())
for i in range(1, t+1):
    n = int(input())
    print("#{}".format(i))
    sol(n)