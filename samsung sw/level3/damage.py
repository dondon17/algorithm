def solution(d, l, n):
    result = 0
    for i in range(n):
        result += d*(1+(i*l)/100)
    return int(result)


t = int(input())

for i in range(1, t+1):
    d, l, n = map(int, input().split())
    answer = solution(d, l, n)
    print("#{} {}".format(i, answer))