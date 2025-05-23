from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        need = Counter(t)
        have = {}
        have_count = 0
        res = ""
        min_len = float('inf')
        l = 0

        for r in range(len(s)):
            char = s[r]
            have[char] = have.get(char, 0) + 1

            if char in need and have[char] == need[char]:
                have_count += 1

            while have_count == len(need):
                # 최소 길이 갱신
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    res = s[l:r+1]
                
                # 왼쪽 포인터 줄이기
                have[s[l]] -= 1
                if s[l] in need and have[s[l]] < need[s[l]]:
                    have_count -= 1
                l += 1

        return res
