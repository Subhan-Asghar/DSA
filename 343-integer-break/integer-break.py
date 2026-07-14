class Solution:
    def integerBreak(self, n: int) -> int:
        nums=[x for x in range(1,n)]
        memo={}
        def knapsack(W,n):
            if W==0:
                return 1
            if n==0:
                return 0
            if (W,n) in memo:
                return memo[(W,n)]
            if nums[n-1]>W:
                ans=knapsack(W,n-1)
            else:
                take=nums[n-1]*knapsack(W-nums[n-1],n)
                skip=knapsack(W,n-1)
                ans=max(take,skip)
            memo[(W,n)]=ans
            return ans
        return knapsack(n,len(nums))