# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n, val, found = self.dfs(root, 0, k)
        return val


    def dfs(self, root: Optional[TreeNode], n:int, k: int) -> Tuple[int, int, bool]:
        if not root:
            return n, None, False
        
        n_l, res, found = self.dfs(root.left, n, k)
        if found: return n_l, res, found

        if n_l + 1 == k: return n, root.val, True
        
        return self.dfs(root.right, n_l + 1, k)
