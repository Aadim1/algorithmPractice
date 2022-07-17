# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('inf'))
        dummy.next = head
        slow = fast = head
        
        while fast and fast.next:
            dummy = dummy.next
            slow = slow.next
            fast = fast.next.next
    
    
        if dummy.val == float('inf'):
            head = None
    
        if slow.next:
            slow.val = slow.next.val
            slow.next = slow.next.next
        else:
            dummy.next = None
        
        return head
      
      
      # ------------------- V2 -----------------------
      
      class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        slow = fast = head
        count = 0
        while fast and fast.next:
            dummy = dummy.next
            slow = slow.next
            fast = fast.next.next
            count += 1
        
        if count == 0:
            head = None
        else:
            dummy.next = dummy.next.next
        
        return head
