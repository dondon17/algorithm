def solution(pan, n, m):
    ans = 0
    for r in range(n):
        rowcnt = 0
        for c in range(n):
            if pan[r][c] == 1: 
                rowcnt +=1
                if rowcnt == m and c == n-1: 
                    ans+=1
                    break
            elif pan[r][c] == 0:
                if rowcnt == m: ans +=1
                rowcnt =0

    for c in range(n):
        colcnt = 0
        for r in range(n):
            if pan[r][c] == 1:
                colcnt += 1
                if colcnt == m and r == n-1: 
                    ans+=1
                    break
            elif pan[r][c] == 0:
                if colcnt == m: ans+=1
                colcnt = 0
    return ans
            

t = int(input())

for i in range(1, t+1):
    answer = 0
    n, k = map(int, input().split())
    pan = []
    for j in range(n):
        pan.append(list(map(int, input().split())))
    answer = solution(pan, n, k)
    print("#{} {}".format(i, answer))