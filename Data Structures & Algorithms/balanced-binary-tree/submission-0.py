# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        height, ans = self.isBalancedAux(root)
        return ans
        
    def isBalancedAux(self, root: Optional[TreeNode]) -> Tuple[int, bool]:
        if not root:
            return 0, True
        
        left_h, left_b = self.isBalancedAux(root.left)
        right_h, right_b = self.isBalancedAux(root.right)

        difference = abs(left_h - right_h) <= 1
        return max(left_h, right_h) + 1, difference and left_b and right_b
