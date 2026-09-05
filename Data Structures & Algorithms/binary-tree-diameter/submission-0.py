# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, diameter = self.dfs(root)
        return diameter
        
    def dfs(self, root: Optional[TreeNode]) -> List[int, int]:
        
        if not root:
            return 0, 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        depth_left, depth_right = left[0], right[0]
        diameter_left, diameter_right = left[1], right[1]

        depth = max(depth_left, depth_right)
        maxDiameter = max(diameter_left, diameter_right)
        diameter = max(depth_left + depth_right, maxDiameter)

        return [1 + depth, diameter]


        
