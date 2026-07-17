class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result=[intervals[0]]
        n=len(intervals)
        for i in range(1,n):
            first=result[-1]
            second=intervals[i]
            if first[1]>=second[0]:
                ans=[min(first[0],second[0]),max(first[1],second[1])]
                result[-1]=ans
            else:
                result.append(second)
        return result