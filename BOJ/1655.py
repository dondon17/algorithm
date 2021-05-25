import sys, heapq

r = sys.stdin.readline
n = int(r())

left = []
right = []

for _ in range(n):
    tmp = int(r())

    if len(left) == len(right):
        heapq.heappush(right, (-tmp, tmp))
    else:
        heapq.heappush(left, (tmp, tmp))

    if left and right[0][1] > left[0][1]:  
        rightNum = heapq.heappop(right)[1]
        leftNum = heapq.heappop(left)[1]

        heapq.heappush(right, (-leftNum, leftNum))
        heapq.heappush(left, (rightNum, rightNum))
    
    print(right[0][1])