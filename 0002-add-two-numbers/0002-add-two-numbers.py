# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2, i=0, 0, 0
        while l1:
            num1+=l1.val*(10**i)
            i+=1
            l1=l1.next
        i=0
        while l2:
            num2+=l2.val*(10**i)
            i+=1
            l2=l2.next
        
        total=num1+num2
        answer=ListNode(-1)
        start=answer

        while total!=0:
            num=total%10
            answer.next=ListNode(num)
            answer=answer.next
            total//=10
        
        if not start.next: return ListNode(0)
        
        return start.next