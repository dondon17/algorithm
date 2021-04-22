def solution(direction):
    a, b = 1, 1
    for d in direction:
        if d=='L':
            b = a+b
        elif d == 'R':
            a = a+b
    return a, b
    
t = int(input())

for i in range(1, t+1):
    answer = 0
    direction = input()
    a, b = solution(direction)
    print("#{} {} {}".format(i, a, b))