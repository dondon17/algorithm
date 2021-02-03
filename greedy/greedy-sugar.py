sugar = int(input())

div5 = sugar // 5
div3 = sugar // 3
_min = 100000

for a in range(div5+1):
    for b  in range(div3+1):
        if sugar == (5*a)+(3*b):
            if a+b<_min:
                _min = a+b

answer = -1 if _min == 100000 else _min

print(answer)