class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        ans = []
        subSet = []

        def dfs(start):
            if start >= len(s):
                ans.append(subSet[:])
                return

            for end in range(start,len(s)):
                sub = s[start:end+1]
                if sub == sub[::-1]:
                    subSet.append(sub)
                    dfs(end+1)
                    subSet.pop()
                
            

        dfs(0)
        print('ans:',ans)
        return ans