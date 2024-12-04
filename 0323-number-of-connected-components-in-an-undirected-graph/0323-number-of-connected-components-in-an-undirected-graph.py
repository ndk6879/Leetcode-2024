class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connect = {}
        for i in range(n):
            connect[i] = []
        for a,b in edges:
            connect[a].append(b)
            connect[b].append(a)
            
        visit = set()
        print('connect:',connect)
        def dfs(i):
            if connect[i] == []: 
                print('i:',i)
                # return True
            elif i in visit: return False


            visit.add(i)
            for a in connect[i]:
                dfs(a)
            return True

        ans = 0
        for i in range(n):
            if dfs(i):
                ans += 1
    
        return ans
        