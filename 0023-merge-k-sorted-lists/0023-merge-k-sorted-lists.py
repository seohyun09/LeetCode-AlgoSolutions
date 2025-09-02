# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        que=PriorityQueue()
        for i in range(len(lists)):
            while lists[i]:
                que.put(lists[i].val)
                lists[i]=lists[i].next
        node=ListNode(-1)
        start=node
        while not que.empty():
            node.next=ListNode(que.get())
            node=node.next
        return start.next