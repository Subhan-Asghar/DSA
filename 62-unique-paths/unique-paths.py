class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo={}
        def func(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return 0
            if i==m-1 and j==n-1:
                return 1
            if (i,j) in memo:
                return memo[(i,j)]
            # Move
            down=func(i+1,j)
            right=func(i,j+1)
            
            ans=down+right
            memo[(i,j)]=ans
            return ans
        return func(0,0)