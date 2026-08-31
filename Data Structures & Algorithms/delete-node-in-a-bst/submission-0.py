# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            if root.left and not root.right:
                return root.left
            if not root.left and root.right:
                return root.right
            
            
            minVal = self.findMinimum(root.right)
            root.val = minVal

            root.right = self.deleteNode(root.right, minVal)

        return root

    def findMinimum(self, root: Optional[TreeNode]) -> int:
        while root and root.left:
            root = root.left
        return root.val