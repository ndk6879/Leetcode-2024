class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set('aeiou')
        count = 0

        for i in range(len(word)):
            seen = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break  # 모음이 아닌 문자가 있으면 중단
                seen.add(word[j])
                if len(seen) == 5:  # 모든 모음이 포함되었는지 확인
                    count += 1

        return count