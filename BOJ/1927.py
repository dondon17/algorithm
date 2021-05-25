import heapq
import sys

r = sys.stdin.readline
n = int(r().strip())

heap = []

for _ in range(n):
    tmp = int(r().strip())
    if tmp == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, tmp)
