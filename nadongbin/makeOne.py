dp = [0]*30001

n = int(input())

for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if i%2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    elif i%3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    elif i%5 == 0:
        dp[i] = min(dp[i], dp[i//5]+1)

print(dp[n])