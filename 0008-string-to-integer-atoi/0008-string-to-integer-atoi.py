class Solution:
    def myAtoi(self, strs):
        minValue = -2**(31)
        maxValue = 2**(31)-1

        s = strs.strip()
        

        i = 0
        sign = 1
        ans = ''
        while(i<len(s)):
            if s[i] == '+' and i == 0:
                sign = 1

            elif s[i] == '-' and i == 0:
                sign = -1

            elif s[i].isdigit():
                ans += s[i] 
            
            else:
                break
            i += 1
            

        total = 0
        for i in ans:
            total = total*10 + ord(i) - ord('0')

        return max(minValue, min(sign*total,maxValue) )