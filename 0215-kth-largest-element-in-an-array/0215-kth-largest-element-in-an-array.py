import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        while (k > 0):
            cur = heapq.heappop(nums)
            k -= 1

            if k == 0:
                return -cur