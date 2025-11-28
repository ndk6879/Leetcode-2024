class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1 = 0 #dp[i-1]
        rob2 = 0 #dp[i-2]
        

        
        for n in nums:
            temp = max(rob1,rob2 + n)
            rob2 = rob1
            rob1 = temp
        return max(rob1,rob2)