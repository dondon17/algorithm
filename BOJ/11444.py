import sys
my = sys.stdin.readline

n = int(my().strip())
d = [0 for i in range(n+1)]
d[1] = 1
p = 1000000007


def fibo(n):
    if n <= 1:
        return d[n]
    elif n > 1:
        if d[n] != 0:
            return d[n]*p
        else: 
            return fibo(n-1)+fibo(n-2)

print(fibo(n))
