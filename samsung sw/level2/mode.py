import collections

def solution(scores):
    data = collections.Counter(scores)
    data_list = dict(data)
    max_value = max(list(data.values()))
    mode_val = [num for num, freq in data_list.items() if freq == max_value]
    return max(mode_val)

t = int(input())
for i in range(1, t+1):
    n = int(input())
    scores = list(map(int, input().split()))
    answer = solution(scores)
    print("#{} {}".format(i, answer))