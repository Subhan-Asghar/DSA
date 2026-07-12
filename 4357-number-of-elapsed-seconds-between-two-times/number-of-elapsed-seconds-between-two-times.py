class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start=startTime.split(":")
        end=endTime.split(":")

        first=int(start[0])*3600+int(start[1])*60+int(start[2])
        second=int(end[0])*3600+int(end[1])*60+int(end[2])
        return abs(second-first)