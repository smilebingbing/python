# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1=ListNode(0)
        head2=ListNode(0)
        phead1=head1
        phead2=head2
        while head:
            if head.val<x:
                phead1.next=head
                phead1=phead1.next
            else:
                phead2.next=tmp
                phead2=phead2.next
            head=head.next
        phead2.next=None
        phead1.next=head2.next
        return head1.next