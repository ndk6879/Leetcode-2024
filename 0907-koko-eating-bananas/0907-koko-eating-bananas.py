class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        ans = r

        while(l<=r):
            k = (l+r)//2
            cur = 0

            for pile in piles:
                cur += ceil(pile / k)
            

            if cur <= h:
                print('cur:',cur)
                ans = k
                r = k - 1
            
            else:
                l = k + 1

        return ans
                