class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        crsMap = {}

        for i in range(numCourses):
            crsMap[i] = []


        for crs, preq in prerequisites:
            crsMap[crs].append(preq)

        visit = set()
        def dfs(crs):
            if crsMap[crs] == []: 
                return True

            if crs in visit:
                return False

            visit.add(crs)
            for preq in crsMap[crs]:
                if not dfs(preq):
                    return False
            visit.remove(crs)
            crsMap[crs] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True