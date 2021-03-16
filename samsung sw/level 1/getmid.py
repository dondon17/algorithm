def solution(nums):
    nums.sort()
    idx = len(nums)//2
    return nums[idx]

n = int(input())
arr = list(map(int, input().split()))
answer = solution(arr)

print(answer)

           