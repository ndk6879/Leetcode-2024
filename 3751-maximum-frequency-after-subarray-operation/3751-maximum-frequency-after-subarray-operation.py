class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        
        ans1 = nums.count(k)
        ans2 = 0

        for i in range(1,51):
            if i == k: continue

            frequency = 0
            for num in nums:

                if num == i:
                    frequency += 1

                elif num == k:
                    frequency -= 1
                
                frequency = max(frequency,0)
                
                ans2 = max(ans2, frequency)
        
        return ans1 + ans2