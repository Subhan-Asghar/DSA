class Solution:
    def jump(self, nums: List[int]) -> int:
        # memo={}
        # def func(index):
        #     if index==len(nums)-1:
        #         return 0
        #     if index in memo:
        #         return memo[index]
        #     ans=float('inf')
        #     for i in range(1,nums[index]+1):
        #         if index+i>=len(nums):
        #             continue
        #         ans=min(ans,func(index+i)+1)
        #     memo[index]=ans
        #     return ans
        # return func(0)
        n=len(nums)
        dp=[float('inf')]*n
        dp[n-1]=0
        for i in range(n-2,-1,-1):
            for jump in range(1,nums[i]+1):
                if i+jump<n:
                    dp[i]=min(dp[i],dp[jump+i]+1)
        return dp[0]