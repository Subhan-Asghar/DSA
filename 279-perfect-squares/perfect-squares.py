class Solution:
    def numSquares(self, n: int) -> int:
        nums=[]
        i=1
        while i * i <= n:
            nums.append(i * i)
            i += 1
        def knapsack(remain):
            if remain==0:
                return 0
            if remain in memo:
                return memo[remain]
            ans=float('inf')
        
            for n in nums:
                if n>remain:
                    break
                ans=min(ans,1+knapsack(remain-n))
            memo[remain]=ans
            return ans
        memo={}
        return knapsack(n)