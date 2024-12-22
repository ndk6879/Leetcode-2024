class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = {}

        for i in s1:
            if i not in s1Count:
                s1Count[i] = 1
            else:
                s1Count[i] += 1

        s2Count = {}
        l = 0
        for i in range(len(s2)):

            if s2[i] not in s2Count:
                s2Count[s2[i]] = 1

            else:
                s2Count[s2[i]] += 1

            print('s2Count:',s2Count)

            while i + 1 - l > len(s1):
                s2Count[s2[l]] -= 1
                if s2Count[s2[l]] == 0:
                    del s2Count[s2[l]]
                l += 1

            if s2Count == s1Count:
                return True

        return False
