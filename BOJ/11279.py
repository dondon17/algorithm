import sys
import heapq

r = sys.stdin.readline

n = int(r())
heap = []

for _ in range(n):
    tmp = int(r().strip())
    if tmp == 0:
        if not heap: # heap이 빈 경우
            print(0)
        else:        # heap이 비어 있지 않은 경우, 최대 값 출력
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-tmp, tmp)) # heap에 -tmp를 우선순위로 tmp 값을 push

