class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while(l < r):
            while l<r and not s[l].isalpha() and not s[l].isdigit():
                l += 1

            while l<r and not s[r].isalpha() and not s[r].isdigit():
                r -= 1
            
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1

            else:
                print('s[l]:',s[l])
                print('s[r]:',s[r])
                return False

            
        return True