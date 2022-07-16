# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        
        def inorderHelper(helperRoot: Optional[TreeNode]):
            if helperRoot:
                inorderHelper(helperRoot.left)
                answer.append(helperRoot.val)
                inorderHelper(helperRoot.right)
        
        inorderHelper(root)
        
        return answer
