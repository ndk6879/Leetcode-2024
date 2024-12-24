class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap = {0 : 1}
        diff = 0
        total = 0
        ans = 0

        for num in nums:
            total += num
            ans += hashMap.get(total - k, 0)
            hashMap[total] = hashMap.get(total, 0) + 1
        return ans
