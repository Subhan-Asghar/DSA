class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        n=len(nums)
        # def knapsack(W,n):
        #     if W==0:
        #         return True
        #     if n==0:
        #         return False
        #     if nums[n-1]>W:
        #         if knapsack(W,n-1):
        #             return True
        #     else:
        #         if knapsack(W-nums[n-1],n-1):
        #             return True
        #         if knapsack(W,n-1):
        #             return True
        #     return False
        # return knapsack(target,n)
        
        dp=[False]*(target+1)
        dp[0]=True
        for i in range(n):
            for w in range(target, nums[i] - 1, -1):
                take=dp[w - nums[i]]
                skip=dp[w]

                dp[w] = take or skip
        return dp[target]
