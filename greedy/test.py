# # 입력하고 싶은만큼 숫자를 입력해 바로 배열에 넣는 방법
# arr = [int(x) for x in input().split()] 

# for num in arr:
#     if num==0: break
#     else: print(num)

# x = int(input(), 16)
# for i in range(1, 16):
#     print("%X*%X=%s" %(x, i, format(x*i, 'X')))

# dp = [0, 1, ]
# n = int(input())
# for i in range(2, n+1):
#     dp.append(dp[i-1]+dp[i-2])

# print(dp[n])

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = nums1+nums2
        if res==[]:
            return 0
        res.sort()
        mid = len(res)//2
        return float(res[mid]) if len(res)%2!=0 else float(res[mid-1]+res[mid])/2
       

s = Solution()
l1 = [1,3]
l2 = [2,4]
l3 = s.findMedianSortedArrays(l1, l2)
print(l3)
        