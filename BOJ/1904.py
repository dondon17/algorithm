# 동적 프로그래밍 - 01타일

import sys
r = sys.stdin.readline
n = int(r())

p = 1000001
dp = [0]*p

for i in range(1, n+1):
    if i<=2: 
        dp[i] = i
    else:
        dp[i] = (dp[i-2]+dp[i-1])%15746

print(dp[n])

''' 
- 문제풀이
1. n=1, n=2 ... 일때를 고려해보면 d(n) = d(n-2)+d(n-1)인 것을 알 수 있음
2. 동적 프로그래밍 방식의 피보나치 수열 방식으로 해결
'''