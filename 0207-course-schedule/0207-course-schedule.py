class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = {}
        for num in range(numCourses):
            courses[num] = []

        for crs, preq in prerequisites:
            courses[preq].append(crs)

        visit = set()
        def dfs(i):
            if courses[i] == []: return True
            if i in visit: return False
            
            visit.add(i)
            for preq in courses[i]:
                if not dfs(preq): return False
            visit.remove(i)
            courses[i] = []
            return True

        for num in range(numCourses):
            if not dfs(num):
                return False

        return True