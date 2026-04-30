class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        '''
        - check if num - 1 exist
        - check how long the consecutive each num is 
        '''

        if nums == []: return 0

        numSet = set(nums)
        ans = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 0
                tmp = 1

                while num+tmp in numSet:
                    length += 1
                    tmp += 1

                
                ans = max(ans,length)
            
        return ans + 1