class Solution:
    def rob(self, nums: List[int]) -> int:
        def knapsack(n):
            if n<=0:
                return 0
            if n in memo:
                return memo[n]
            take=nums[n-1]+knapsack(n-2)
            skip=knapsack(n-1)
            ans=max(take,skip)
            memo[n]=ans
            return ans
        memo={}
        return knapsack(len(nums))