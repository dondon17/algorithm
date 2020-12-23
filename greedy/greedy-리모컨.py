# 그리디 - 리모컨
count = 0 
a, b = map(int, input().split())
while a != b:
    if b-a >= 8:
        a+=10
    elif b-a <= -8:
        a-=10
    elif b-a >= 3:
        a+=5
    elif b-a <= -3:
        a-=5
    elif b-a >= 1:
        a+=1
    elif b-a >= -2:
        a-=1

    count += 1

print(count)
