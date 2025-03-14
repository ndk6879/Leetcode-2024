class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        res = [False] * (len(s)+1)
        res[-1] = True
        print('res:',res)

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:

                if s[i:i+len(word)] == word:
                    res[i] = res[i+len(word)]

                #이게 없으면 이미 True였다 False로 업데이트 될수도 있어서 하는게 좋음.
                if res[i]:
                    break

        return res[0]