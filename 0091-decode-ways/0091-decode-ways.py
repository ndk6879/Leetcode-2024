class Solution:
    def numDecodings(self, s: str) -> int:
        arr = [0] * (len(s)+1)
        if s[0] == '0':
            return 0

        arr[0] = 1
        arr[1] = 1

        #226, [1,1,0,0]
        for i in range(2,len(s)+1):
            if '0' < s[i-1] <= '9':
                arr[i] += arr[i-1]

            if '10' <= s[i-2:i] <= '26':
                arr[i] += arr[i-2]
            
        return arr[-1]