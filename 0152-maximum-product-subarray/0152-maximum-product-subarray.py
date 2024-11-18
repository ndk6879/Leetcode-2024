class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        max가 될 수 있는 경우는 1. num 그자체 2. 아니면 curMax * num 3. 아니면 num * Min
        min이 될수있는 경우도 똑같음. 근데 max가 업데이트 되서 tmp를 위에서 생성하는거임
        
        '''
        ans = max(nums)
        curMax, curMin = 1,1
        for num in nums:
            tmp = curMax*num
            curMax = max(num, curMax*num,curMin*num) 
            curMin = min(num, tmp,curMin*num)
            ans = max(ans, curMax)
        return ans