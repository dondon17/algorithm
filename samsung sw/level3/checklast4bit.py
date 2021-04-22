def solution(a, b):
    if b == 0 or a < 1 or a > 30: return "OFF"

    cnt = 0
    while(b > 0):
        if b%2 == 0:
            break
        elif b%2 == 1: 
            cnt += 1    
            if cnt == a: break
        b//=2

    if cnt==a: return "ON"
    else: return "OFF"
    
    


t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    answer = solution(n, m)
    print("#{} {}".format(i, answer))