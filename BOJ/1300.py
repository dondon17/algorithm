import sys
put = sys.stdin.readline

n = int(put())
k = int(put())

low = 0
high = k

answer = 0
while low <= high:
    mid = (low+high)//2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(mid//i, n)

    if cnt < k:
        low = mid+1
    else:
        answer = mid
        high = mid-1

print(answer)