# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.pathAux(root, 0, targetSum)

    def pathAux(self, root: Optional[TreeNode], val: int, targetSum: int) -> bool:
        if not root.left and not root.right:
            if val + root.val == targetSum:
                return True
            return False

        if root.left:
            if self.pathAux(root.left, root.val + val, targetSum):
                return True
        if root.right:
            if self.pathAux(root.right, root.val + val, targetSum):
                return True
        return False
        