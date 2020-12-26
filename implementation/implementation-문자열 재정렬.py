n = input()
nw = []
sum = 0
res = ""

for i in n:
    # if ord(i)<=90 and ord(i)>=65: 
    if i.isalpha():
        nw.append(i)
    else:
        sum += int(i)

nw.sort()
if sum != 0:
    nw.append(str(sum))

print(''.join(nw))

