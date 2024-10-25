class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        - dfs
        - crs : preq
        - if no preq: return True
        '''

        visit = set()
        def dfs(num):
            if adict[num] == []:
                return True
            
            if num in visit:
                return False

            visit.add(num)    
            for i in adict[num]:
                if not dfs(i): return False
            visit.remove(num)
            adict[num] = []

            return True


        adict = {}
        for i in range(numCourses):
            adict[i] = []

        for crs, preq in prerequisites:
            adict[crs].append(preq) 

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        print('adict:',adict)