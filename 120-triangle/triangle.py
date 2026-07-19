class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        memo={}
        def func(index,i):
            if index==n:
                return 0
            if (index,i) in memo:
                return memo[(index,i)]
            same=triangle[index][i]+func(index+1,i)
            plus=float("inf")
            if i<len(triangle[index])-1:
                plus=triangle[index][i+1]+func(index+1,i+1)
            ans=min(same,plus)
            memo[(index,i)]=ans
            return ans
        return func(0,0)
