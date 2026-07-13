class Solution:
    def jump(self, nums: List[int]) -> int:
        memo={}
        def func(index):
            if index==len(nums)-1:
                return 0
            if index in memo:
                return memo[index]
            ans=float('inf')
            for i in range(1,nums[index]+1):
                if index+i>=len(nums):
                    continue
                ans=min(ans,func(index+i)+1)
            memo[index]=ans
            return ans
        return func(0)