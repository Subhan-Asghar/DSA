class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo={}
        def knapsack(W,n):
            if W==0:
                return 0
            if n==0:
                return float('inf')
            if (W,n) in memo:
                return memo[(W,n)]
            if coins[n-1]>W:
                ans=knapsack(W,n-1)
            else:
                take=1+knapsack(W-coins[n-1],n)
                skip=knapsack(W,n-1)
                ans=min(take,skip)
            memo[(W,n)]=ans
            return ans
        result = knapsack(amount,len(coins))
        return result if result!=float('inf') else -1