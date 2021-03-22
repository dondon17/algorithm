
t = int(input())
for i in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    print("#{} {}".format(i, ' '.join(str(x) for x in nums)))
    