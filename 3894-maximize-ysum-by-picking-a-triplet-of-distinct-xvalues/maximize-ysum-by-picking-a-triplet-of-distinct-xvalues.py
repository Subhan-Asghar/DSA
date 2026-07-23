import heapq as hq
class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        heap=[(-x,i) for i ,x in enumerate(y)]
        hq.heapify(heap)
        seen=set()
        total_sum=0
        while heap and len(seen)!=3:
            val,index=hq.heappop(heap)
            if x[index] not in seen:
                total_sum+=-val
                seen.add(x[index])
            if len(seen)==3:
                return total_sum
        return -1