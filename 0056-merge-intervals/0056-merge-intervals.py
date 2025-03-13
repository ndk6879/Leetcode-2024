class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur = intervals[0]
        ans = []

        for i in range(1,len(intervals)):
            if cur[0] > intervals[i][1]:
                ans.append(cur)

            elif cur[1] < intervals[i][0]:
                ans.append(cur)
                cur = intervals[i]

            else:
                cur = [min(cur[0],intervals[i][0]), max(cur[1], intervals[i][1])]
        ans.append(cur)
        return ans