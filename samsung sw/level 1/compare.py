t = int(input())

for i in range(1, t+1):
    a, b = map(int, input().split())
    answer = "=" if a == b else (">" if a > b else "<")
    
    print("#%d %s" %(i, answer))
