# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        index=1
        list1=ListNode(-1)
        start=list1
        while head:
            if left==right:
                return head
            elif index<left:
                list1.next=ListNode(head.val)
                list1=list1.next
            elif index==left:
                list2=ListNode(head.val)
                list2_head=list2
            elif index<right:
                node=ListNode(head.val)
                node.next=list2
                list2=node
            elif index==right:
                node=ListNode(head.val)
                node.next=list2
                list2=node
                list1.next=list2
                list1=list2_head
            else:
                list1.next=ListNode(head.val)
                list1=list1.next
            head=head.next
            index+=1
        return start.next


