# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, visit, result = [root], [False], []


        while stack:
            curr = stack.pop()
            v = visit.pop()

            if not curr:
                continue

            if v == False:
                stack.append(curr)
                visit.append(True)

                stack.append(curr.right)
                visit.append(False)

                stack.append(curr.left)
                visit.append(False)
            else:
                result.append(curr.val)
        
        return result