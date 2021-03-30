t = int(input())

for i in range(1, t+1):
    answer = 0
    n = int(input())
    v = 0
    for _ in range(n):
        cmd = list(map(int, input().split()))

        if cmd[0] == 1: v += cmd[1]
        elif cmd[0] == 2: 
            if v <= cmd[1]: v = 0
            else: v -= cmd[1]
        
        answer += v
    print("#{} {}".format(i, answer))   