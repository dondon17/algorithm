n, m = map(int, input().split())

def sol(n, m):
    if n == 1:
        if m == 1:
            return 0
        else:
            return m-1
    
    elif n > 1:
        if m == 1:
            return n-1
        else:
            return (n-1) + n * (m-1)
    
print(sol(n,m ))