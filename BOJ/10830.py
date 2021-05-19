'''
행렬의 n제곱을 구하는 문제 - 미완
'''

import sys
myinput = sys.stdin.readline

def multipleMatrix(m1, m2):
    ab = [[0]*len(m1) for _ in range(len(m2))]
    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m1[0])):
                ab[i][j] += m1[i][k]* m2[k][j]  
                ab[i][j] %= 1000
    return ab

n, b = map(int, myinput().split())
matrix = [list(map(int, myinput().split())) for _ in range(n)]
answer = [[1 if i == j else 0 for i in range(n)]for j in range(n)]


while b > 1:
    temp = matrix[:]
    if b%2 == 1:
        # b가 홀수인 경우, 단위행렬을 곱해줌
        answer = multipleMatrix(temp, answer)
        b -= 1
    elif b%2 == 0:
        # 만약 b가 짝수이면, matrix를 제곱해줌
        matrix = multipleMatrix(temp, temp)
        b //= 2

answer = multipleMatrix(matrix, answer)
for row in answer:
    print(*row)