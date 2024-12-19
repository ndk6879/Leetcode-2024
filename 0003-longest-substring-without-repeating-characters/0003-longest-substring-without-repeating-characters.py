class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        string = ''
        for i in s:
            string += i
            while len(string) != len(set(string)): #만약 새로 추가된 i가 이미 string에 있다면
                string = string[1:] #string의 크기를 줄임. 언제까지? string의 모든문자가 unique할때까지 (while loop을 씀으로서)
            ans = max(ans, len(string))
        return ans