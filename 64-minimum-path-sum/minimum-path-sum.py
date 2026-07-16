class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def func(i,j):
            if i<0 or j<0 or i>=r or j>=c:
                return float('inf')
            if i==r-1 and j==c-1:
                return grid[i][j]
            if (i,j) in memo:
                return memo[(i,j)]
            down=func(i+1,j)
            right=func(i,j+1)
            ans=min(down,right)+grid[i][j]
            memo[(i,j)]=ans
            return ans
        memo={}
        return func(0,0)