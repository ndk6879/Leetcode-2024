class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        from collections import Counter

        counter = Counter(words)
        ans = 0
        odd = False
        
        for word, count in counter.items():
            reversedWord = word[::-1]
            if word == reversedWord:
                ans += (count//2) * 4
                if count % 2 == 1:
                    print('odd')
                    odd = True

            elif word > reversedWord:
                print('dsa')
                ans += min(count, counter[reversedWord]) * 4
        if odd:
            ans += 2
        return ans