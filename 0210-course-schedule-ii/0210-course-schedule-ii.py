class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        crsMap = {}
        for i in range(numCourses):
            crsMap[i] = []

        for crs, preq in prerequisites:
            crsMap[crs].append(preq)

        visit = [0] * numCourses
        def dfs(i):
            if visit[i] == 1:
                return False

            if visit[i] == 2:
                return True

            visit[i] = 1
            for preq in crsMap[i]:
                if not dfs(preq): return False
            visit[i] = 2
            ans.append(i)
            return True

        ans = []
        for i in range(numCourses):
            if not dfs(i):
                return []

        return ans