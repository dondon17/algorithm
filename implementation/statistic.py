from collections import Counter

n = int(input())
arr = []
cnt = [0 for _ in range(n)]

for _ in range(n):
    arr.append(int(input()))

arr.sort()
cnt= Counter(arr)
modes = cnt.most_common()
if n > 1:
    if modes[0][1] == modes[1][1]:
        _mode = modes[1][0]
    else: 
        _mode = modes[0][0]
else:
    _mode = modes[0][0]

_mean = round(sum(arr)/len(arr))
_mid = arr[n//2] #ok
_range = max(arr)-min(arr)

print(_mean)
print(_mid)
print(_mode)
print(_range)
