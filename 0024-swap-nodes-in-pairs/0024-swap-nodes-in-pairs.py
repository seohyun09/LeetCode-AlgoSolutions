# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        answer=ListNode(0, None)
        start=answer

        while True:
            num1=head.val
            if not head.next:
                answer.next=ListNode(num1)
                return start.next
            
            head=head.next
            num2=head.val
            
            answer.next=ListNode(num2)
            answer=answer.next
            answer.next=ListNode(num1)
            answer=answer.next
            
            if head.next:
                head=head.next
            else:
                break
        
        return start.next