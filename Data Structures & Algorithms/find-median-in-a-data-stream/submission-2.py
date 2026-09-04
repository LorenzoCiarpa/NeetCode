class MedianFinder:

    def __init__(self):
        self.small, self.large  = [], []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.small, -1 * num)
        if self.small and self.large and (-1 * self.small[0] > self.large[0]):
            tmp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        
        if len(self.small) > len(self.large) + 1:
            tmp = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, tmp)
        if len(self.large) > len(self.small) + 1:
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * tmp)
        
        return


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        
        tmp_small = -1 * self.small[0]
        return (tmp_small + self.large[0]) / 2
        
        