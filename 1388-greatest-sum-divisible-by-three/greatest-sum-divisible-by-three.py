class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        memo={}
        def func(i,val):
            if i==len(nums):
                if val==0:
                    return 0
                return -float("inf")
            if (i,val) in memo:
                return memo[(i,val)]
            take=nums[i]+func(i+1,(val+nums[i])%3)
            skip=func(i+1,val)
            ans=max(take,skip)
            memo[(i,val)]=ans
            return ans
        return func(0,0)