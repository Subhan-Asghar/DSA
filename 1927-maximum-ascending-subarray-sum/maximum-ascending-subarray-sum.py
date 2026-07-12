class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_ans=0
        low=0
        total_sum=0
        for high in range(len(nums)):
            if high>0 and nums[high]<=nums[high-1]:
                low=high
                total_sum=0
            total_sum+=nums[high]
            max_ans=max(max_ans,total_sum)
        return max_ans
