class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adict = {}
        for i in range(numCourses):
            adict[i] = []
        
        for crs, preq in prerequisites:
            adict[crs].append(preq)

        visit = set()
        print('adict:',adict)
        def dfs(crs):
            if adict[crs] == []: return True
            if crs in visit: return False

            visit.add(crs)
            print('adict[crs]:',adict[crs])
            for preq in adict[crs]:
                if not dfs(preq): return False
            visit.remove(crs)  
            adict[crs] = []
            return True
        
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True