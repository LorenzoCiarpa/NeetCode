# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.inorderTraversalAux(root, arr)
        return arr

    def inorderTraversalAux(self, root: Optional[TreeNode], arr) -> List[int]:
        if not root:
            return
        
        self.inorderTraversalAux(root.left, arr)
        arr.append(root.val)
        self.inorderTraversalAux(root.right, arr)
        return
    
        