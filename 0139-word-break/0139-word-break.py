class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False] * (len(s)+1)
        res[-1] = True
        print('res:',res)

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:

                if i + len(word) <= len(s) and s[i:i+len(word)] == word:
                    print(s[i:i+len(word)] , word)
                    print(res,'\n')
                    res[i] = res[i+len(word)]

                if res[i]:
                    break

        return res[0]