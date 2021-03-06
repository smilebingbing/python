# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head==None:
            return head
        if k==0:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        count=0
        while p.next:
            p=p.next
            count+=1
        p.next=dummy.next
        k=k%count
        for i in range(count-k):
            p=p.next
        head=p.next
        p.next=None
        return head
