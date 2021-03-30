def solution(num):
    check = [0]*10
    j = 2
    tmp = num

    while True:

        for i in sorted(list(int(e) for e in str(tmp))):
            if check[i] == 0: check[i] = 1
            else: continue

        if 0 not in check: 
            return tmp
        tmp = num*j
        j += 1
        
    return -1

t = int(input())

for i in range(1, t+1):
    n = int(input())
    answer = solution(n)
    print("#{} {}".format(i, answer))