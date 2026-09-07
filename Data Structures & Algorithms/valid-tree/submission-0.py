class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
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
            self.countComponents(adj, u, visit)
        
        if counter > 1:
            return False
        
        # Verify cycles
        visit = set()
        cycles = self.hasCycles(adj, 0, visit, None)
        if cycles:
            return False
        
        return True
    
    def countComponents(self, adj, u, visit):
        visit.add(u)
        for node in adj[u]:
            if node not in visit:
                self.countComponents(adj, node, visit)
    
    def hasCycles(self, adj, u, visit, prev):
        if u in visit:
            return True

        visit.add(u)
        
        for node in adj[u]:
            if node == prev:
                continue
            val = self.hasCycles(adj, node, visit, u)
            if val:
                return True


        return False