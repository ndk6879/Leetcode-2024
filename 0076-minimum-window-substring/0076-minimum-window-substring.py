from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        have = {}
        haveCount = 0

        ans = ''
        ansLen = float("inf")

        l = 0
        for r in range(len(s)):
            have[s[r]] = have.get(s[r],0) + 1

            c = s[r]
            if c in need and have[c] == need[c]:
                haveCount += 1

            
            #조건이 충족되면
            while ( haveCount == len(need) ):
                # 값 비교
                if (r + 1 - l) < ansLen:
                    ansLen = r + 1 -l
                    ans = s[l:r+1]

                #왼쪽 포인터 길이 조절
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    haveCount -= 1

                l+=1

        return ans