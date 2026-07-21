import heapq as hq
class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        heap=[-x for x in nums]
        hq.heapify(heap)
        total_sum=0
        for _ in range(k):
            val=-hq.heappop(heap)
            if mul>0:
                total_sum+=val*mul
                mul-=1
            else:
                total_sum+=val
        return total_sum
