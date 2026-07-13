class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax=nums[0]
        globalMax=nums[0]
        currMin=nums[0]
        globalMin=nums[0]

        for i in range(1,len(nums)):
            currMax=max(currMax+nums[i],nums[i])
            globalMax=max(currMax,globalMax)
            currMin=min(currMin+nums[i],nums[i])
            globalMin=min(currMin,globalMin)
        total=sum(nums)
        return max(globalMax,total-globalMin) if globalMax>0 else globalMax
