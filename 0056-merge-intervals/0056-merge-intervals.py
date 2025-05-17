class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # S. 이끌기 0. 어떻게 풀지 method 생각  1. edge case 2. psuedo code 3. TC#
        intervals.sort()
        ans = []
        cur = intervals[0]

        for i in range(1,len(intervals)):

            #1. if overlap
            if cur[1] >= intervals[i][0]:
                cur = [ min(cur[0], intervals[i][0])   , max(cur[1],intervals[i][1]) ]

            #2. not overlap -> compare interval and cur 
            elif cur[1] < intervals[i] [0]:
                ans.append(cur)
                cur = intervals[i]


        ans.append(cur)
        return ans