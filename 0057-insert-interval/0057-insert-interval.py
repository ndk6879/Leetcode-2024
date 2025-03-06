class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        cur = newInterval
        ans = []

        for i in range(len(intervals)):
            
            #Not Overlap 1
            if intervals[i][1] < cur[0]:
                ans.append(intervals[i])
                print('ans:',ans)

            #Not Overlap 2
            elif intervals[i][0] > cur[1]:
                ans.append(cur)
                return ans + intervals[i:]

            #Overlap 
            else:
                cur = [min(intervals[i][0], cur[0]), max(intervals[i][1] ,cur[1])]
                print('cur:',cur)
        ans.append(cur)
        return ans