class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
        - Use two pointer variables l,r at 0, len(s) - 1 index for each
        - check if character at eaach index is character. If not, go to next one or change it to lower alphabet
        - check if they are different and return False
        - if they meet, just return True 
        '''


        l,r = 0, len(s) - 1
        
        while (l < r):
            while l < r and  not s[l].isalnum():
                l += 1
            
            while l < r and    not s[r].isalnum():
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        return True