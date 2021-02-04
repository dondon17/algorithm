n = int(input())
neg = []
pos = []
exc = []

for i in range(n):
    tmp = int(input())
    if tmp == 0 or tmp == 1: exc.append(tmp)
    elif tmp > 1: pos.append(tmp)
    else: neg.append(tmp)

pos.sort(reverse=True)
neg.sort()

plen = len(pos)
nlen = len(neg)

result = 0

if plen%2 == 0:
    for i in range(0, plen-1, 2):
        result += pos[i]*pos[i+1]

elif plen%2 == 1:
    for i in range(0, plen-1, 2):
        result += pos[i]*pos[i+1]
    result += pos[-1]


if nlen%2 == 0:
    for i in range(0, nlen-1, 2):
        result += neg[i]*neg[i+1]

elif nlen%2 == 1:
    for i in range(0, nlen-1, 2):
        result += neg[i]*neg[i+1]
    if 0 not in exc:
        result += neg[-1]

result+=sum(exc)

print(result)
    