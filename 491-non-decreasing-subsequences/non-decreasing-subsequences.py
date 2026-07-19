class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result=[]
        n=len(nums)
        def backtrack(index,path):
            if len(path)>1:
                result.append(path[:])
            used=set()
            for i in range(index,n):
                if nums[i] in used:
                    continue
                if path and path[-1]>nums[i]:
                    continue
                used.add(nums[i])
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return result