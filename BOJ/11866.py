# 요세푸스 문제
n, k = map(int, input().split())

persons = list(i for i in range(1, n+1))
answer = []


# 1. 원래 리스트에서 K 번째 사람을 -1로 바꾸고 answer에 추가
# 2. 빠진 사람 다음부터 다시 k번째 사람을 -1로 바꾸고 answer에 추가
# 3. 

idx = 0
for _ in range(n):  
    cnt = 0
    while True: 
        if idx >= n: 
            idx = 0
        if persons[idx] == -1:
            idx += 1    
            continue
        cnt += 1
        if cnt == k:
            answer.append(persons[idx])
            persons[idx] = -1
            cnt = 0
            idx += 1
            break
        else: 
            idx+=1
            continue

print("<", end="")
for i in range(n):
    if i != n-1:
        print(answer[i], end=", ")
    else:
        print(answer[i], end="")
print(">")