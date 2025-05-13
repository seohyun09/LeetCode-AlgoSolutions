# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        node=ListNode(0)
        node.next=head
        start=node

        while node.next and node.next.next:
            a=node.next
            b=node.next.next

            a.next=b.next
            node.next=b
            node.next.next=a
            
            node=node.next.next
        
        return start.next