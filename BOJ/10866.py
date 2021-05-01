from collections import deque

import sys


'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

n = int(input())
q = deque([])

for _ in range(n):
    cmd = list(sys.stdin.readline().split())
    if "push_front" == cmd[0]:
        q.appendleft(int(cmd[1]))
    elif "push_back" == cmd[0]:
        q.append(int(cmd[1]))
    elif "pop_front" == cmd[0]:
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif "pop_back" == cmd[0]:
        if not q:
            print(-1)
        else:
            print(q.pop())
    elif "size" == cmd[0]:
            print(len(q))
    elif "empty" == cmd[0]:
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif "front" == cmd[0]:
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif "back" == cmd[0]:
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])


