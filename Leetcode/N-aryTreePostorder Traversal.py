"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        
        def postorderHelper(helperRoot: 'Node'):
            if helperRoot:
                for children in helperRoot.children:
                    postorderHelper(children)
                answer.append(helperRoot.val)
        postorderHelper(root)
        return answer
