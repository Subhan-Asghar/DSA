class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        memo={}
        def func(i,j):
            if i<0 or j<0 or i>=r or j>=c or  obstacleGrid[i][j]==1:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if i==r-1 and j==c-1:
                return 1
            down=func(i+1,j)
            right=func(i,j+1)
            ans=down+right
            memo[(i,j)]=ans
            return ans
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        return func(0,0)
