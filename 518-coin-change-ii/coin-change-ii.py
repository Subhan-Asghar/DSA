class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def knapsack(W,n):
            if W==0:
                return 1
            if n==0:
                return 0
            if (W,n) in memo:
                return memo[(W,n)]
            if coins[n-1]>W:
                ans=knapsack(W,n-1)
            else:
                ans=knapsack(W-coins[n-1],n)+knapsack(W,n-1)
            memo[(W,n)]=ans
            return ans
        memo={}
        return knapsack(amount,len(coins))