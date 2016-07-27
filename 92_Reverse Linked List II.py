"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None





"""
 S1 : 
  逆置m-n  之间Node 
  1. 找到m 前驱
  2. 将m-n  之间的头插
  3. 记住标记m 点， 最后将m.next  = n 后面的


"""
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        my_head = ListNode(0)  #head
        my_head.next = head

        if m == n :
            return head
        pre_m = my_head  #m pre
        i = 1 
        while i <m: 
            pre_m = pre_m.next
            i +=1
        last = pre_m.next  #m
        p = last.next
        while i <n :
            tmp = p.next
            p .next = pre_m.next
            pre_m.next =  p
            p = tmp
            i +=1
        last.next = p
        return my_head.next  

        










if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next=ListNode(3)
    s = Solution()
    r = s.reverseBetween(l1,2,3)
    while r:
       print(r.val)
       r = r.next
