"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        
        def preorderHelper(helperRoot: 'Node'):
            if helperRoot:
                answer.append(helperRoot.val)
                for children in helperRoot.children:
                    preorderHelper(children)
        preorderHelper(root)
        return answer
