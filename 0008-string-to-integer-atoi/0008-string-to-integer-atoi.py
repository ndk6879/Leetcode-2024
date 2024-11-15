class Solution:
    def myAtoi(self, strs):
        minValue = -2**(31)
        maxValue = 2**(31)-1

        s = strs.strip()
        

        i = 0
        sign = 1
        ans = 0
        while(i<len(s)):
            if s[i] == '+' and i == 0:
                sign = 1

            elif s[i] == '-' and i == 0:
                sign = -1

            elif s[i].isdigit():
                print('strs[i]:',s[i])

                ans = ans * 10 + int(s[i])
            
            else:
                break
            i += 1
            
        ans = ans * sign

        return max(min(maxValue, ans), minValue)