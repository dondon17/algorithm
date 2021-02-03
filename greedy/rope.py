def solution(_arr):
    _arr.sort(reverse=True)
    answer = _arr[0]

    for i, w in enumerate(_arr):
        if answer <= w*(i+1):
            answer = w*(i+1)
    return answer

n = int(input())
weights = []

for _ in range(n):
    weights.append(int(input()))

weights.sort(reverse=True)
_max = weights[0]

print(solution(weights))
