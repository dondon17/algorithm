import sys

r = sys.stdin.readline

N = int(r())
dist = list(map(int, r().split()))
prices = list(map(int, r().split()))

answer = prices[0] * dist[0]
basePrice = prices[0]

for i in range(1, len(prices)-1):
    if prices[i] <= basePrice:
        basePrice = prices[i]
    answer += dist[i]*basePrice

print(answer)