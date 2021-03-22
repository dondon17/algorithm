def solution(word, c, n):
    tmp = ""
    for i in range(10):
        
        
t = int(input())
for i in range(1, t+1):
    answer = ""
    n = int(input())
    for _ in range(n):
        ch, num = input().split()
        answer += solution(answer, ch, num)
    print("#{} {}".format(i, answer))