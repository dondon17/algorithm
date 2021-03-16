t = int(input())

for i in range(1, t+1):
    answer = 0

    n  = int(input())
    prices = list(map(int, input().split()))
    last = prices[-1]
    
    for j in range(len(prices)-1, -1, -1):
        if last > prices[j]: answer += last-prices[j]
        else: last = prices[j]
    
    print("#%d %d" %(i, answer))