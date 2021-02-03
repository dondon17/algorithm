n = int(input())
arr = []
alpha = [0 for _ in range(26)]

for _ in range(n):
    arr.append(input())

arr.sort(key=lambda x: len(x), reverse=True)

for _str in arr:
    for i in range(len(_str)):
        alpha[ord(_str[i])-ord('A')] += pow(10, len(_str)-(i+1))

alpha.sort(reverse=True)
answer = 0
count = 9

for num in alpha:
    if num != 0:
        answer += num*count
        count -= 1
    
    if count == 0:
        break

print(answer)