"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = {}
        newNode = self.cloneAux(node, visit)
        return newNode
    
    def cloneAux(self, node, visit):
        if not node:
            return None

        if node.val in visit:
            return visit[node.val]

        newNode = Node(node.val)
        visit[node.val] = newNode

        for n in node.neighbors:
            newNeigh = self.cloneAux(n, visit)
            if newNeigh:
                newNode.neighbors.append(newNeigh)
        
        return newNode

    # def graphSize(self, node) -> int:
    #     visit = set()
    #     queue = deque()

    #     queue.append(node)
    #     count = 0

    #     while queue:
    #         for _ in range(len(queue)):
    #             curr = queue.popleft()
    #             visit.add(curr)
    #             count += 1

    #             for n in curr.neighbors:
    #                 if n not in visit:
    #                     queue.append(n)
                
    #     return count


    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if not node:
    #         return None

    #     visit = set()
    #     queue = deque()

    #     queue.append(node)

    #     graphSize = self.graphSize(node)
    #     result = [Node(i + 1) for i in range(graphSize)]


    #     while queue:
    #         for _ in range(len(queue)):
    #             curr = queue.popleft()
    #             visit.add(curr)
    #             idx = curr.val - 1

    #             for n in curr.neighbors:
    #                 if n not in visit:
    #                     queue.append(n)
                    
    #                 result[idx].neighbors.append(result[n.val-1])
    #     return result[0]
        