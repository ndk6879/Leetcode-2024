class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        while(len(s) > 2):
            tmp = ''

            for i in range(1,len(s)):
                cur = (int(s[i-1]) + int(s[i])) % 10
                tmp += str(cur)
                # print('tmp:',tmp, int(s[i-1]) + int(s[i]))

            s = tmp

        return s[0] == s[1]