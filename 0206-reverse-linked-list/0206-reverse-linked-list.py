# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        reverse=ListNode(-1, None)
        start=reverse
        
        while head:
            stack.append(head.val)
            head=head.next
        
        while stack:
            num=stack.pop()
            node=ListNode(num, None)
            reverse.next=node
            reverse=reverse.next
        
        return start.next


        