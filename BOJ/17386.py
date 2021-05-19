import sys
myinput = sys.stdin.readline

x11,y11,x12,y12 = map(int, myinput().split())
x21,y21,x22,y22 = map(int, myinput().split())


def check(x11,y11,x12,y12,x21,y21,x22,y22):
    f1= (x12-x11)*(y21-y11) - (y12-y11)*(x21-x11)
    f2= (x12-x11)*(y22-y11) - (y12-y11)*(x22-x11)
    if f1*f2 < 0: return True
    else: return False

def solution(x11,y11, x12,y12, x21,y21, x22,y22):
    b1 = check(x11,y11, x12,y12, x21,y21, x22,y22)
    b2 = check(x21,y21, x22,y22, x11,y11, x12,y12)
    if b1 and b2: return 1
    else: return 0


print(solution(x11,y11, x12,y12, x21,y21, x22,y22))