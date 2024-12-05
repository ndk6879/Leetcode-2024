class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        arr = [0] * (len(s)+1)
        arr[0] = 1 # s가 뭐시기 다른 문자거나 빈거일경우라는데 모르겟네
        arr[1] = 1 # s의 첫부분

        for i in range(2,len(s)+1):
            #한자리수 확인
            if '0' < s[i-1] <= '9':
                arr[i] += arr[i-1]
            
            #두자리수 확인
            if '10' <= s[i-2:i] <= '26':
                arr[i] += arr[i-2]
            
        return arr[-1]