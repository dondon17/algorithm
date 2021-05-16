import sys
myinput = sys.stdin.readline

a, b, c = map(int, myinput().split())

def solution(a, b, c):
    if b == 0:
        return 1
    
    if b % 2 == 1:
        return (solution(a, b-1, c)*a)%c
    else:
        return (solution(a, b//2, c)**2)%c

print(solution(a,b,c))