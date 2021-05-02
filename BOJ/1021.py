'''
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 
둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.
'''

from collections import deque

n, m = map(int, input().split())
order = list(map(int, input().split()))
queue = deque(list(i for i in range(1, n+1)))

answer = []
cnt = 0


for e in order:
    if queue[0] == e:
        queue.popleft()
        continue
    
    idx = queue.index(e)
    if queue.index(e) > len(queue)//2:
        queue.rotate(len(queue)-idx)
        cnt += len(queue)-idx
    elif queue.index(e) <= len(queue)//2:
        queue.rotate(-idx)
        cnt += idx
    queue.popleft()

print(cnt)