class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = 0
        while(l<=r):
            tmp = 0
            k = (l+r)//2

            
            for pile in piles:
                tmp += ceil(pile/k)
            print('tmp:',tmp)
            if tmp <= h:
                ans = k
                r = k - 1
            
            else:
                l = k + 1
            
            print('ans:',ans, l, r)
        return ans