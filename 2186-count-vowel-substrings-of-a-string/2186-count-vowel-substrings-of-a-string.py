class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        a = set('aeiou')
        
        ans = 0
        for i in range(len(word)):
            cur = set()
            for j in range(i,len(word)):
                if word[j] not in a:
                    break
                cur.add(word[j])
                if len(cur) == 5: ans += 1
        return ans