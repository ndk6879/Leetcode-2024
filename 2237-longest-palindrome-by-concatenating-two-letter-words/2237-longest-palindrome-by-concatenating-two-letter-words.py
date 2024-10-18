from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        counter = Counter(words)
        ans = 0
        odd = False

        for word, count in counter.items():
            reverse_word = word[::-1]
            if word == reverse_word:  # 같은 두 글자로 이루어진 단어 (예: "cc")
                ans += (count // 2) * 4  # 쌍을 만들 수 있으면 그 길이를 추가
                if count % 2 == 1:
                    odd = True  # 홀수 개가 있다면 중앙에 넣을 수 있음
            elif word < reverse_word:  # 같은 단어가 아니고, 사전순으로 한 번만 처리
                pairs = min(count, counter[reverse_word])
                ans += pairs * 4  # 쌍으로 팰린드롬의 양 끝을 채움

        if odd:
            ans += 2  # 중앙에 넣을 단어가 있으면 추가

        return ans
