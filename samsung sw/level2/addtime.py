def sol(h1, m1, h2, m2):
    if m1 < 0 or m1 > 59 or m2 <0 or m2 > 59 or h1 < 1 or h1 > 12 or h2 < 1 or h2 > 12:
        return -1, -1
    h, m = 0, 0
    if m1+m2 >= 60:
        m = m1+m2-60
        h += 1
    else:
        m = m1+m2
	
    if h1+h2 > 12:
        if h1+h2 > 23: h += h1+h2-23
        else: h += h1+h2-12
    else: h+= h1+h2
    return h, m

t = int(input())

for i in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())
    h, m = sol(h1, m1, h2, m2)
    
    print("#{} {} {}".format(i, h, m))