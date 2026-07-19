class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        def backtrack(index,path):
            if len(path)>1 and path not in result:
                result.append(path[:])
            for i in range(index,n):
                if path and path[-1]>nums[i]:
                    continue
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return result