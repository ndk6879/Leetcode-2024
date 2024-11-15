class Solution:
    def myAtoi(self, strs):
        min_value = (-2)**31 
        max_value = (2)**31 - 1
        strs = strs.strip()

        i = 0
        sign = 1
        ans = ''
        non_int = 0
        while (i < len(strs)):
            if i ==0 and strs[i] == '-':
                sign = -1    

            elif  i ==0 and strs[i] == '+':
                sign = +1
                
            elif strs[i].isdigit():
                ans += str(strs[i])

            else:
                break

            i+= 1
        if ans == '':
            return (0)
        return (max(min_value, min(sign * int(ans), max_value)))
