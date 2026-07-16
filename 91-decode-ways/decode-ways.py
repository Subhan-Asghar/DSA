class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        memo={}
        def func(i):
            if i>n:
                return 0
            if i==n:
                return 1
            if i in memo:
                return memo[i]

            if s[i]=='0':
                return 0
            ans=func(i+1)
            if i+1<n and 10<=int(s[i:i+2]) <=26:
                ans+=func(i+2)
            memo[i]=ans
            return ans
        return func(0)

