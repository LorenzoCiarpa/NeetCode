class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, p):
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]        
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p2] = p1
            self.rank[p1] += 1
        
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        stack = []
        unionFind = UnionFind(len(edges))
        for edge in edges:
            res = unionFind.union(edge[0], edge[1])
            
            if not res:
                stack.append(edge)
        return stack.pop()