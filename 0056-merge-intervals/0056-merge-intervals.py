class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = []
        cur = intervals[0]
        for i in range(1,len(intervals)):
            if cur[1] >= intervals[i][0]:
                cur = [min(cur[0], intervals[i][0]), max(cur[1], intervals[i][1])]
                print('cur:',cur)
            
            else:
                arr.append(cur)
                cur = intervals[i]

        arr.append(cur)
        return arr