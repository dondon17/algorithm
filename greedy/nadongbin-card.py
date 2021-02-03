# 2차원 배열의 각 행에서 가장 작은 수들 중에서 최대 값을 구하는 문제
# 입력한 2차원 배열을 반드시 저장해야할 필요는 없다!!

n, m = map(int, input().split(" "))
answer = 0

for _ in range(n):
    row = list(map(int, input().split(" ")))
    _min = min(row)
    answer = max(answer, _min)

print(answer)