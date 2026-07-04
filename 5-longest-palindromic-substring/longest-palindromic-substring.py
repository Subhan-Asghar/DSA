class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def expend(left,right):
            while left>=0 and right<n and s[left]==s[right]:
                left-=1
                right+=1
            return [left+1,right-1]
        start=0
        end=0
        for i in range(n):
            l1,r1=expend(i-1,i+1)
            l2,r2=expend(i,i+1)
            if r1-l1>end-start:
                start=l1
                end=r1
            if r2-l2>end-start:
                start=l2
                end=r2
        return s[start:end+1]