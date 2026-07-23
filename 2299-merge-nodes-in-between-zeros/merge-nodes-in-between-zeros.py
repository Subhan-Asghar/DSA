# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        c=dummy
        prev=-1
        curr=head
        while curr and curr.next:
            nxt=curr.next
            if curr.val==0:
                c.next=ListNode()
                c=c.next
            else:
                c.val+=curr.val
            curr=nxt
        return dummy.next
