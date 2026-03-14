class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        '''
        1. find num that can be a starting element for consequence (i.e. no preceding)
        2. find the length
        '''

        numSet = set(nums)
        ans = 0
        for num in numSet:
            length = 1
            if num-1 not in numSet:
                

                while (num+length) in numSet:
                    length += 1
                
            ans = max(ans,length)
        return ans