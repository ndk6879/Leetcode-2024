class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        curEnd = intervals[0][1]
        ans = 0

        for start,end in intervals[1:]:
            
            if curEnd <= start:
                curEnd = end

            else:
                ans += 1
                curEnd = min(curEnd,end)

        return ans