class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = 0
        ans = 0

        while (l<=r):
            print(l,r)
            tmp = 0
            k = (l+r)//2
            for pile in piles:
                tmp += ceil(pile/k)
            
            if tmp <= h:
                ans = k
                print('ans:',ans)
                r = k - 1

            else:
                l = k + 1
        return ans     
        