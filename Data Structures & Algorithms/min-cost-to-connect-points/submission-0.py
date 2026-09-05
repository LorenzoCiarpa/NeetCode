class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst = []
        minHeap = []
        visit = set()


        for j in range(1, len(points)):
            p1 = points[0]
            p2 = points[j]

            dist = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
            heapq.heappush(minHeap, (dist, 0, j))
        
        visit.add(0)

        while minHeap:
            dist, u, v = heapq.heappop(minHeap)
            if v in visit:
                continue
            
            visit.add(v)

            for j in range(len(points)):
                if j != v and j not in visit:
                    p1 = points[v]
                    p2 = points[j]
                    newDist = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
                    heapq.heappush(minHeap, (newDist, v, j))
            mst.append(dist)
        
        return sum(mst)