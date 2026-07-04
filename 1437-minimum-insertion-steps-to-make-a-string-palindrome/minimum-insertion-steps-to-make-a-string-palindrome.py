class Solution:
    def minInsertions(self, s: str) -> int:
        s2=s[::-1]
        if s==s2:
            return 0
        memo={}
        def lcs(m,n):
            if m==0 or n==0:
                return 0
            if (m,n) in memo:
                return memo[(m,n)]
            ans=0
            if s[m-1]==s2[n-1]:
                ans=1+lcs(m-1,n-1)
            else:
                ans=max(lcs(m-1,n),lcs(m,n-1))
            memo[(m,n)]=ans
            return ans
        m=len(s)
        return m-lcs(m,m)