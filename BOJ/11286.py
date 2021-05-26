import sys, heapq

r = sys.stdin.readline

n = int(r().strip())

heap = []

for _ in range(n):
    tmp = int(r().strip())
    if tmp == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(tmp), tmp))
