class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        print('intervals:',intervals)
        cur = intervals[0]
        ans = []


        for i in range(1,len(intervals)):

            #1. NOT overlap
            if cur[1] < intervals[i][0]:
                ans.append(cur)
                cur = intervals[i]

            #2. not 
            elif cur[0] > intervals[i][1]:
                ans.append(cur[i])


            #3. overlap
            
            else:
                cur = [min(cur[0], intervals[i][0]), max(cur[1], intervals[i][1])]
        ans.append(cur)
        return ans