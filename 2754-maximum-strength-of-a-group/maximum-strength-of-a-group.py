import math
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        result=nums[0]
        n=len(nums)
        def func(index,path):
            nonlocal result
            if path:
                result=max(result,math.prod(path))
            for i in range(index,n):
                path.append(nums[i])
                func(i+1,path)
                path.pop()
        func(0,[])
        return result
