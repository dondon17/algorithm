def sol(p):
    answer = ""
    flag = 0
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            if p[i:j] == p[j:2*j-i]:
                answer += p[i:j]
                flag = 1
                break
        if flag == 1: break
    return answer, len(answer)



t = int(input())
for i in range(1, t+1):
    p = input()
    ans, l = sol(p)
    print("#%d %d" %(i, l))