def getGCD(n, m):
    while m != 0:
        r = n%m
        n = m
        m = r
    return n

def getLCM(n, m):
    return (n*m)//getGCD(n, m)

n, m = map(int, input().split())
print(getGCD(n, m), getLCM(n, m))
