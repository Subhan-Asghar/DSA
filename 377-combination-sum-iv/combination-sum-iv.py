class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def knapsack(remain):
            if remain==0:
                return 1
            if remain in memo:
                return memo[remain]
            ans=0
            for i in nums:
                if i>remain:
                    continue
                ans+=knapsack(remain-i)
            memo[remain]=ans
            return ans
        memo={}
        return knapsack(target)