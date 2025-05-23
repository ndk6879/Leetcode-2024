class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        

        cur = []
        res = []

        def dfs(i):
            if i == len(s):
                tmp = ' '.join(cur)
                res.append(tmp)
                return

            for j in range(i,len(s)):
                string = s[i:j+1]
                if string in wordDict:
                    cur.append(string)
                    dfs(j+1)
                    cur.pop()

        dfs(0)

        return res