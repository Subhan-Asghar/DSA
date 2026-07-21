import heapq as hq
class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        total_sum=0
        for i in range(k):
            val=nums[i]
            if mul>0:
                total_sum+=val*mul
                mul-=1
            else:
                total_sum+=val
        return total_sum
