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
        