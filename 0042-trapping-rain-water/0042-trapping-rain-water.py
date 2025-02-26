class Solution:
    def trap(self, height: List[int]) -> int:
        if height == 0: return 0

        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        ans = 0

        #height의 각 위치에서 값은 min(maxL,maxR) - height[i]. min(maxL, maxR)로 구해야 index 4,5에서 알맞은 값을 구할수있음.
        while(l<r):
            if maxL < maxR:
                l += 1
                maxL = max(maxL,height[l])
                ans += maxL - height[l]

            else:
                r -= 1
                maxR = max(maxR, height[r])
                ans += maxR - height[r]
        return ans