# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        hashMap = dict()
        i = 0
        while head:
            hashMap[i] = head
            head = head.next
            i += 1
        
    
        answer = 0
        
        for index in range(i//2):
            twin = (i - 1 - index)
            answer = max(answer, hashMap[index].val + hashMap[twin].val)
        return answer
