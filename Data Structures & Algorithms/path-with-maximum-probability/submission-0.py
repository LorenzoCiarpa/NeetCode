class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}

        for i in range(0, n):
            adj[i] = []
        
        for i, (ui, vi) in enumerate(edges):
            adj[ui].append((vi, succProb[i]))
            adj[vi].append((ui, succProb[i]))
        
        shortest = {}
        maxHeap = [(-1, start_node)]

        while maxHeap:
            p1, u = heapq.heappop(maxHeap)
            p1 = -1 * p1

            if u in shortest:
                continue
            
            shortest[u] = p1


            for v, p2 in adj[u]:
                if v not in shortest:
                    heapq.heappush(maxHeap, (-1 * (p1 * p2), v))
        

        if end_node not in shortest:
            return 0
        return shortest[end_node]