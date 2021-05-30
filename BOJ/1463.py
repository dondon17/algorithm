# 동적 프로그래밍 - 1로 만들기

import sys
r = sys.stdin.readline

n = int(r())
p = pow(10, 6)+1
dp = [0]*p

def solution(n):
    for i in range(2,n+1):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2]+1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3]+1)
    return dp[n]

print(solution(n))

''' 
- 문제풀이 
1. 문제에서 주어진 N의 최대 값만큼 0 배열 생성
2. dp[2] ~ dp[n] 까지의 값들을 dp[i] = dp[i-1]+1로 초기화
3. 2로 나눴을 때, 3으로 나눴을 때, 최소값이 되는 값으로 dp[i] 업데이트
4. 인덱스 n 까지 반복

'''