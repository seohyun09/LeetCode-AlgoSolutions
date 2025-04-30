# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def lengthOfList(head):
            length=0
            while head:
                length+=1
                head=head.next
            return length

        length=lengthOfList(head)
        stack=[]

        for i in range(length//2):
            stack.append(head.val)
            head=head.next
        
        if length==0 or length==1:
            return True
        elif length%2==1:
            head=head.next

        for i in range(length//2):
            num=stack.pop()
            if num!=head.val:
                return False
            head=head.next

        return True