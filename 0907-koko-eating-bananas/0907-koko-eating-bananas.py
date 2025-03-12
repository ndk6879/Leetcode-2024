class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        ans = 0

        while(l<=r):
            k = (l + r ) // 2
            tmp = 0
            
            for pile in piles:
                tmp += ceil(pile / k)
            
            if tmp <= h:
                ans = k
                r = k - 1

            else:
                l = k + 1
            
        return ans