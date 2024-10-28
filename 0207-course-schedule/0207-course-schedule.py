class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        visitSet = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(num):
            if preMap[num] == []:
                return True
            
            if num in visitSet:
                print('visited')
                return False
            
            visitSet.add(num)
            for n in preMap[num]:
                if not dfs(n): return False
            visitSet.remove(num)
            preMap[num] = []
            return True

        for n in range(numCourses):
            if not dfs(n):
                print('not dfs')
                return False
        return True