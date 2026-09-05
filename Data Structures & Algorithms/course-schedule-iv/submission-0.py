class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {}

        for i in range(numCourses):
            adj[i] = []
        
        for a, b in prerequisites:
            adj[a].append(b)
        
        results = []
        for query in queries:
            start_node, end_node = query
            visit = set()

            result = self.dfs(adj, start_node, end_node, visit)
            results.append(result)

        return results


    def dfs(self, adj, start_node, end_node, visit) -> bool:
        
        if start_node in visit:
            return False
        
        if start_node == end_node:
            return True
        
        visit.add(start_node)
        result = False
        for dst in adj[start_node]:
            result = result or self.dfs(adj, dst, end_node, visit)
            if result:
                return result
        return result