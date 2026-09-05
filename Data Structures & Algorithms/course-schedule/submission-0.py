class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for i in range(numCourses):
            adj[i] = []
        
        for a, b in prerequisites:
            adj[a].append(b)
        
        visit = set()
        path = set()
        topSort = []
        for n in range(numCourses):
            result = self.dfs(adj, n, visit, topSort, path)
            if not result:
                return False
        return True


    def dfs(self, adj, src, visit, topSort, path) -> bool:
        if src in path:
            return False
        if src in visit:
            return True
        
        
        visit.add(src)
        path.add(src)
        for dst in adj[src]:
            result = self.dfs(adj, dst, visit, topSort, path)
            if not result:
                return result
        
        path.remove(src)
        topSort.append(src)
        return True
