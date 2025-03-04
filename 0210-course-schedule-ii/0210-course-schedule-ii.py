class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        crsMap = {}

        for i in range(numCourses):
            crsMap[i] = []
        
        for crs, preq in prerequisites:
            crsMap[crs].append(preq)


        visit = [0] * (numCourses)
        ans = []
        def dfs(i):
            if visit[i] == 1: return False
            if visit[i] == 2: return True

            visit[i] = 1
            for pre in crsMap[i]:
                if not dfs(pre): return False

            visit[i] = 2
            ans.append(i)
            return True

        for n in range(numCourses):
            if not dfs(n): return []

        return ans