class Solution(object):
    def removeDuplicates(self,nums):
        a=0
        l=len(nums)
        i=0
        while i<l:
            nums[a]=nums[i]
            a+=1
            i+=1
            while i<l and nums[i]==nums[i-1]:
                i+=1
        return a
'''
1. 思想：因为是排好序的，所以去掉重复的元素，就是将一次循环过程中，
         不重复的元素按序排在列表的前n个位置，这时就需要一个初始设置值
         来标记位置。
'''