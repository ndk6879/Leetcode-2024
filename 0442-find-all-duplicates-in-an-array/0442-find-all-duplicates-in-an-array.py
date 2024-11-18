class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        adict = {}
        for num in nums:
            if num in adict:
                adict[num] += 1

            else:
                adict[num] = 1

        ans = []
        for k in adict:
            if adict[k] > 1:
                ans.append(k)
        return ans