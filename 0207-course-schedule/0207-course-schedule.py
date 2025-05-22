class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        crsMap = {}

        for i in range(numCourses):
            crsMap[i] = []

        for crs, pre in prerequisites:
            crsMap[crs].append(pre)
        
        visit = set()
        def dfs(i):
            if crsMap[i] == []: return True
            if i in visit: return False

            visit.add(i)
            for crs in crsMap[i]:
                if not dfs(crs): return False

            visit.remove(i)
            crsMap[i] = []
            return True

        for i in crsMap:
            if not dfs(i): return False
        
        return True
