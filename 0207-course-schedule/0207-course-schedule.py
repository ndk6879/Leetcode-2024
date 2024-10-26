class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crsMap = {}
        for i in range((numCourses)):
            crsMap[i] = []
        
        for crs,preq in prerequisites:
            crsMap[crs].append(preq)

        for i in crsMap:
            print('i:',i,crsMap[i])
            
        visitSet = set()
        def dfs(num):
            if crsMap[num] == []:
                return True
            
            if num in visitSet:
                return False

            visitSet.add(num)
            for preq in crsMap[num]:
                if not dfs(preq):
                    return False
            visitSet.remove(num)
            crsMap[num] = []
            return True

        for num in crsMap:
            if not dfs(num):
                return False
        return True