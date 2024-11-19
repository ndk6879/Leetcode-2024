class Solution:
    def myAtoi(self, s: str) -> int:
        ans = 0
        sign = 1
        s = s.strip()
        minAns = - 2 ** 31
        maxAns = (2**31) - 1
        for i in range(len(s)) :
            
            if i == 0 and s[i] == '+':
                sign = 1
            elif i == 0 and s[i] == '-':
                sign = -1
            elif s[i].isdigit():
                ans = ans * 10 + ord(s[i]) - ord('0')

            elif not s[i].isdigit(): break
        return max(minAns,min(sign*ans, maxAns))