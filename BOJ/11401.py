'''
(n k) = n! / k!(n-k)!
'''

import sys, math
myinput = sys.stdin.readline

p = 1000000007

def pow(a, b):
    if b == 0:
        return 1
    if b % 2 == 1: 
        return (pow(a, b-1)*a) % p
    else:
        return (pow(a, b//2)**2) % p


n, k = map(int, myinput().split())
d = [1 for _ in range(n+1)]

for i in range(2, n+1):
    d[i] = i*d[i-1]%p

factN = d[n]
factK = d[k]
factNK = d[n-k]

print((factN%p)*(pow((factNK*factK)%p, p-2)%p)%p)
