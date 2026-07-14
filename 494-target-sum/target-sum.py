class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # def knapsack(W,n):
        #     if n==0:
        #         if W==0:
        #             return 1
        #         return 0
        #     if nums[n-1]>W:
        #         ans=knapsack(W,n-1)
        #     else:
        #         nega=knapsack(W-nums[n-1],n-1)
        #         plus=knapsack(W+nums[n-1],n-1)
        #         ans=nega+plus
        #     return ans
        # return knapsack(target,len(nums))
        memo={}
        def func(W,n):
            if n==len(nums):
                if W==target:
                    return 1
                return 0
            if (W,n) in memo:
                return memo[(W,n)]
            plus=func(W+nums[n],n+1)
            nega=func(W-nums[n],n+1)
            ans=plus+nega
            memo[(W,n)]=ans
            return ans
        return func(0,0)


