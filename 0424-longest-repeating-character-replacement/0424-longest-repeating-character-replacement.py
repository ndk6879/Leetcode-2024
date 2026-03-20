class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        '''
        use two pointers l,r
        increment r by 1
        l += 1 when more than k
        '''

        l,r = 0,0
        hashMap = {}
        ans = 0

        while(r < len(s)):
            hashMap[s[r]] = hashMap.get(s[r],0) + 1

            while (r + 1 - l) - max(hashMap.values()) > k:
                hashMap[s[l]] -= 1
                l += 1

            r += 1
            ans = max(ans,r  -l)
        
        return ans