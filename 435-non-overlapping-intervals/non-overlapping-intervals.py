class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x :x[1])
        count=0
        result=[intervals[0]]
        n=len(intervals)
        for i in range(1,n):
            first=result[-1]
            second=intervals[i]
            if first[1]>second[0]:
                count+=1
            else:
                result.append(intervals[i])
        return count