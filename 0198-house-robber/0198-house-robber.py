'''
rob1, rob2가 dp 배열의 i-2, i-1 인덱스를 가리키고
매 loop마다 오른쪽으로 한 칸씩 이동한다 생각해도 됨
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        rob1 = 0 #dp[i-1]
        rob2 = 0 #dp[i-2]
        

        
        for n in nums:
            temp = max(rob1,rob2 + n)
            rob2 = rob1
            rob1 = temp
        return max(rob1,rob2)