# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        
        if head is None or head.next is None:
            return head

        odd=ListNode(head.val)
        even=ListNode(head.next.val)
        odd_head=odd
        even_head=even
        curr=head.next.next
        location=3

        while curr:
            if location%2==0:
                even.next=ListNode(curr.val)
                even=even.next
            else:
                odd.next=ListNode(curr.val)
                odd=odd.next
            curr=curr.next
            location+=1
        
        odd.next=even_head
        return odd_head
            