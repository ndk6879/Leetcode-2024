class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        

        res = []

        def dfs(i, path):
            if i == len(s):
                tmp = ' '.join(path)
                res.append(tmp)
                return

            for j in range(i,len(s)):
                string = s[i:j+1]
                if string in wordDict:
                    path.append(string)
                    dfs(j+1,path)
                    path.pop()

        dfs(0, [])

        return res