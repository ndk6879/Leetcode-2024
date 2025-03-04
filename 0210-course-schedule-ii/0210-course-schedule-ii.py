class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        crsMap = {}

        for i in range(numCourses):
            crsMap[i] = []
        
        for crs, preq in prerequisites:
            crsMap[crs].append(preq)


        visit = [0] * numCourses
        ans = []
        def dfs(i):
            if visit[i] == 2: return True
            if visit[i] == 1:
                return False

            visit[i] = 1
            for pre in crsMap[i]:
                dfs(preq)

            visit[i] = 2
            ans.append(i)
            crsMap[i] = []
            return True

        for i in range(numCourses):
            dfs(i)


        return ans