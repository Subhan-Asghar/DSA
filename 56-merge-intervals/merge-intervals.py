class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[intervals[0]]

        for i in range(1,len(intervals)):
            first=result[-1]
            second=intervals[i]
            if first[1]>=second[0]:
                ans=[min(first[0],second[0]),max(first[1],second[1])]
                result[-1]=ans
            else:
                result.append(second)
        return result