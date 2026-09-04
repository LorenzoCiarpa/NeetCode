class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, n + 1):
            adj[i] = []
        
        for ui, vi, ti in times:
            adj[ui].append((vi, ti))
        
        shortest = {}
        minHeap = [(0, k)]

        maxElem = 0
        count = 0

        while minHeap:
            t1, u = heapq.heappop(minHeap)

            if u in shortest:
                continue
            
            shortest[u] = t1
            count += 1
            maxElem = max(maxElem, t1)


            for v, t2 in adj[u]:
                if v not in shortest:
                    heapq.heappush(minHeap, (t1 + t2, v))
        

        if count < n:
            return -1
        return maxElem