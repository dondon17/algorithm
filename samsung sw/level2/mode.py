# 이걸 왜 못푸냐 빙신아

def solution(scores):
    score_count = Counter(scores)
    answer = sorted(score_count, key=score_count.get)[-2]
    return answer        

t = int(input())
for testcase in range(1, t+1):
    answer = 0
    scores = list(map(int, input().split()))
    answer = solution(scores)
    print("#{} {}".format(testcase, answer))