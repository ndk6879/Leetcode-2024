class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        arr = [False] * (len(s)+1)
        arr[-1] = True
        
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                # print(s[i:i+len(w)])
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    print(s[i:i+len(w)])
                    arr[i] = arr[i+len(w)]
                if arr[i]:
                    break
        print('arr:',arr)
        return arr[0]
