class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        memo={}
        def func(pos,n):
            if n==k:
                if pos==endPos:
                    return 1
                return 0
            if (pos,n) in memo:
                return memo[(pos,n)]
            
            left=func(pos+1,n+1)
            right=func(pos-1,n+1)
            ans=left+right
            memo[(pos,n)]=ans
            return ans
        return func(startPos,0) %((10**9)+7)
            