# 이걸 왜 못푸냐 빙신아
def solution(scores):
    tmp = [0]*101
    for s in scores:
        tmp[s] += 1

    _max = max(tmp)
    for i in range(100, -1, -1):
        if _max == tmp[i]: 
            return i

    return -1            

t = int(input())
for testcase in range(1, t+1):
    answer = 0
    scores = list(map(int, input().split()))
    answer = solution(scores)
    print("#{} {}".format(testcase, answer))