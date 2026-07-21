class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n=len(arr)
        # memo={}
        # def func(index,prev):
        #     if index==n:
        #         return 0
        #     if (index,prev) in memo:
        #         return memo[(index,prev)]
        #     take=0
        #     not_take=func(index+1,prev)
        #     if prev==-1 or arr[index]-arr[prev]==difference:
        #         take=1+func(index+1,index)
        #     ans=max(take,not_take)
        #     memo[(index,prev)]=ans
        #     return ans
        # return func(0,-1)

        # dp=[1]*n
        # for index in range(1,n):
        #     for prev in range(index):
        #         if arr[index]-arr[prev]==difference:
        #             dp[index]=max(dp[index],dp[prev]+1)
        # return max(dp)
        dp={}
        ans=1
        for x in arr:
            dp[x]=dp.get(x-difference,0)+1
            ans=max(ans,dp[x])
        return ans