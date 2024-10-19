class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        adict = {}

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if (i + j) not in adict:
                    adict[i+j] = []
                adict[i+j].append(nums[i][j])

        ans = []
        for i in adict:
            ans += adict[i][::-1]
        return ans
