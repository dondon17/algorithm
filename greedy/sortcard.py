import heapq

n = int(input())
card = []

for _ in range(n):
    heapq.heappush(card, int(input()))


if len(card) == 1:
    print(0)
else:
    res = 0

    while len(card) > 1:
        first = heapq.heappop(card)
        second = heapq.heappop(card)

        res += first + second
        heapq.heappush(card, first + second)
    
    print(res)

# import heapq 알아두기!
# 스택처럼 사용할 수 있는 것으로 보인다