class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        crsMap = {}

        for i in range(numCourses):
            crsMap[i] = []

        for crs, preq in prerequisites:
            crsMap[crs].append(preq)

        visit = set()
        def dfs(i):
            if crsMap[i] == []: return True
            if i in visit: return False

            visit.add(i)
            for pre in crsMap[i]:
                if not dfs(pre): return False

            visit.remove(i)
            crsMap[i] = []
            return True

        
        for i in range(numCourses):
            if not dfs(i): return False
        
        return True

        