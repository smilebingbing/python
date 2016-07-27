# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        p=dummy
        while head:
            last=head
            i=k
            while head and i>0:
                tmp=head.next
                head.next=p.next
                p.next=head
                head=tmp
                i-=1
            if i>0:
                cur=p.next
                p.next=None
                while cur:
                    tmp=cur.next
                    cur.next=p.next
                    p.next=cur
                    cur=tmp
                return dummy.next
            else:
                p=last
        return dummy.next


        