class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        gap=0
        for i in range(len(nums)-1):
            diff=nums[i+1]-nums[i]
            gap=max(gap,diff)
        return gap