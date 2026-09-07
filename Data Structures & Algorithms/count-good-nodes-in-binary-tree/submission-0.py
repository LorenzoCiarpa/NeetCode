# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxNode = - float("inf")
        return self.dfs(root, maxNode)

        
    def dfs(self, root: Optional[TreeNode], maxNode: int) -> int: 
        if not root:
            return 0
        
        counter = 0

        if root.val >= maxNode:
            counter += 1
        
        maxNode = max(maxNode, root.val)
        
        counter += self.dfs(root.left, maxNode)
        counter += self.dfs(root.right, maxNode)

        return counter