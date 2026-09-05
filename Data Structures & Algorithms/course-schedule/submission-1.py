class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i in range(numCourses):
            adj[i] = []
        
        for a, b in prerequisites:
            adj[a].append(b)
        
        visit = set()
        path = set()
        for n in range(numCourses):
            result = self.dfs(adj, n, visit, path)
            if not result:
                return False
        return True


    def dfs(self, adj, src, visit, path) -> bool:
        if src in path:
            return False
        if src in visit:
            return True
        
        
        visit.add(src)
        path.add(src)
        for dst in adj[src]:
            result = self.dfs(adj, dst, visit, path)
            if not result:
                return result
        
        path.remove(src)
        return True
