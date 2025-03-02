class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1*num)

        #make sure every value in small heap <= every value in large heap
        if (self.small and self.large) and self.small[0] * -1 > self.large[0]:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val*-1)
        
        #for uneven size
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val*-1)
        
        elif len(self.small) +1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val*-1)
        


    def findMedian(self) -> float:
        # print('HEAP:',self.small,self.large)
        if len(self.small) > len(self.large):
            return self.small[0] * -1

        elif len(self.small) < len(self.large):
            return self.large[0]

        return ((self.small[0] * -1) + self.large[0]) / 2

        
        

        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()