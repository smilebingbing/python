# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None or head.next.next==None:
            return head
        p1=head
        p2=head
        while p1 and p1.next:
            p1=p1.next.next
            p2=p2.next
        head1=head
        head2=p2.next
        p2.next=None
        dummy=ListNode(0)
        dummy.next=head2
        p=head2.next
        while p:
            tmp=p
            p=p.next
            tmp.next=dummy.next
            dummy.next=tmp
        p1=head1
        p2=head2
        while p2:
            tmp1=p1.next
            tmp2=p2.next
            p1.next=p2
            p2.next=tmp1
            p1=tmp1.next
            p2=tmp2.next
            
