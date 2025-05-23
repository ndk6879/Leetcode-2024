class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ans = []
        temp = []

        def dfs(i,path):
            print('path:',path)
            if i >= len(s):
                ans.append(' '.join(path))
                return

            for j in range(i,len(s)):
                cur = s[i:j+1]
                for word in wordDict:
                    if cur == word:
                        print('cur:',cur)
                        path.append(word)
                        dfs(j+1,path)
                        path.pop()

        dfs(0,temp)

        return ans