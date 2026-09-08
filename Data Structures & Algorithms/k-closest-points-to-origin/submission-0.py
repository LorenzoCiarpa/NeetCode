class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for p in points:
            x, y = p[0], p[1]
            dist = math.sqrt(x ** 2 + y ** 2)
            heapq.heappush(minHeap, (dist, p))
        
        result = []
        for i in range(k):
            p = heapq.heappop(minHeap)[1]
            result.append(p)
        
        return result