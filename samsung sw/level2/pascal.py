def solution(n):
    answer = [[1 for _ in range(i)] for i in range(1, n+1)]
    for i in range(2, n):
        for j in range(1, i):
            answer[i][j] = answer[i-1][j-1] + answer[i-1][j]
    
    for e in answer:
        for d in e:
            print(d, end=" ")
        print()

t = int(input())

for i in range(1, t+1):
    n = int(input())
    print("#%d" %i)
    solution(n)
    