class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        crsMap = {}
        for i in range(numCourses):
            crsMap[i] = []

        for crs, pre in prerequisites:
            crsMap[crs].append(pre)

        visit = [0] * numCourses
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


        for i in range(numCourses):
            if not dfs(i): return []
        
        return ans