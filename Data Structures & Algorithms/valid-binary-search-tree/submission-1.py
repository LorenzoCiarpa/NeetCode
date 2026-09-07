# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = self.dfs(root)
        return res[0]

    def dfs(self, root):
        if not root:
            return True, float("inf"), - float("inf")
        
        res_l, min_l, max_l = self.dfs(root.left)
        res_r, min_r, max_r = self.dfs(root.right)

        if not res_l or not res_r:
            return False, 0, 0

        if max_l >= root.val:
            return False, 0, 0
        
        if min_r <= root.val:
            return False, 0, 0
        
        minNode = min(min_l, min_r, root.val)
        maxNode = max(max_l, max_r, root.val)

        return True, minNode, maxNode
