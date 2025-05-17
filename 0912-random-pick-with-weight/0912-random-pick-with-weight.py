import random
import bisect

# random.random()
# random.choice(arr) 
# bisect.bisect_left(arr, element

class Solution:

    def __init__(self, w: List[int]):
        self.proArr = []
        total = 0
        for weight in w:
            total += weight
            self.proArr.append(total)
            #[1,4]


    def pickIndex(self) -> int:
        i = random.random() * self.proArr[-1]
        return bisect.bisect_left(self.proArr,i)
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()