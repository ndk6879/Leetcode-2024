class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = {}
        for i in range(numCourses):
            courses[i] = []
        print('courses:',courses)

        for crs, preq in prerequisites:
            courses[crs].append(preq)

        print('courses:',courses)


        visit = set()
        def dfs(crs):
            if courses[crs] == []: 
                return True

            if crs in visit:
                return False

            visit.add(crs)
            for preq in courses[crs]:
                if not dfs(preq): return False

            visit.remove(crs)
            courses[crs] = []
            return True

            

        for i in range(numCourses):
            if not dfs(i): return False
        return True 
