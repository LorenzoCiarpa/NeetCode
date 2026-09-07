class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for i, (u, v) in enumerate(edges):
            adj[u].append(v)
            adj[v].append(u)
        
        #count components
        visit = set()
        counter = 0
        for u in adj:
            if u in visit:
                continue
            counter += 1
            self.countComponentsAux(adj, u, visit)
        
        return counter
    
    def countComponentsAux(self, adj, u, visit):
        visit.add(u)
        for node in adj[u]:
            if node not in visit:
                self.countComponentsAux(adj, node, visit)