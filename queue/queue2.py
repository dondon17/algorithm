n = int(input())
q = list()
for i in range(n):
    cmd = input()
    if 'push' in cmd:
        q.append(cmd[-1])
        print(q[-1])

    elif cmd=='pop':
        if len(q)==0: print(-1)
        else: print(q.pop())

    elif cmd=='size':
        print(len(q))

    elif cmd=='empty':
        if len(q)==0: print(1)
        else: print(0)

    elif cmd=='front':
        if len(q) == 0: print(-1)
        else: print(q[0])

    elif cmd=='back':
        if len(q) == 0: print(-1)
        else: print(q[-1])
