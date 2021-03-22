def solution(n):
    div = [2,3,5,7,11]
    arr = [0]*5

    while True:
        if n == 1: break
        for i in range(len(div)):
            if n % div[i] == 0:
                n = n//div[i]
                arr[i] += 1
    return arr


t = int(input())
for i in range(1, t+1):
    answer = []
    num = int(input())
    answer = solution(num)
    print("#{}".format(i), end = " ")
    print(*answer, sep = " ")
