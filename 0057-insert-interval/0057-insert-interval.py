class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #안겹칠때
        # if not intervals: return [newInterval]
        ans = []

        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                ans.append(intervals[i])
            
            elif intervals[i][0] > newInterval[1]:
                ans.append(newInterval)
                return ans + intervals[i:]

            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1],newInterval[1])]
        ans.append(newInterval)
        return ans
        #겹칠때
        