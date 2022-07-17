# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        hashMap = dict()
        
        while head:
            hashMap[count] = head
            head = head.next
            count += 1
        return hashMap[count//2]
