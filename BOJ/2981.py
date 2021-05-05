import math
import sys

n = int(sys.stdin.readline())
nums = []
numdif = []
result = []

for i in range(n):
    nums.append(int(input()))

nums.sort()


for i in range(1, n):
    numdif.append(nums[i]-nums[i-1])

numdif.sort()

gcd = numdif[0]
for i in range(1, len(numdif)):
    gcd = math.gcd(gcd, numdif[i])

for i in range(2, gcd+1):
    if gcd%i == 0:
        result.append(i)

print(*result)