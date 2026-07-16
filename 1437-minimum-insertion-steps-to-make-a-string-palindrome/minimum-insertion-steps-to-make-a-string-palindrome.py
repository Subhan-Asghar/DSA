class Solution:
    def minInsertions(self, s: str) -> int:
        s2=s[::-1]
        def func(n,m):
            if n==0 or m==0:
                return 0
            if (n,m) in memo:
                return memo[(n,m)]

            if s[n-1]==s2[m-1]:
                ans=1+func(n-1,m-1)
            else:
                ans=max(func(n-1,m),func(n,m-1))
            memo[(n,m)]=ans
            return ans
        memo={}
        n=len(s)
        return n-func(n,n)