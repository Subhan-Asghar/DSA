class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        m=len(nums2)
        def func(n,m):
            if n==0 or m==0 :
                return 0
            if (n,m) in memo:
                return memo[(n,m)]
            if nums1[n-1]==nums2[m-1]:
                ans=1+func(n-1,m-1)
            else:
                ans=max(func(n-1,m),func(n,m-1))
            memo[(n,m)]=ans
            return ans
        memo={}
        return func(n,m)