"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        answer = [[root.val]]
        
        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            temp = []
            for _ in range(qLen):
                curr = q.popleft()
                for children in curr.children:
                    temp.append(children.val)
                    q.append(children)
            if temp:
                answer.append(temp)
                
        return answer
