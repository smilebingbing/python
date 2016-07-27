class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_p=0
        if len(nums)<2:
            return nums
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                partition=nums[i]
                count_p=i
                break
            if count_p==-1:
                return nums[::-1]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>partition:
                change=nums[i]
                count_c=i
                break
        partition,change=change,partition
        nums[count_p+1:]=nums[count_p+1:][::-1]


'''
 错的
'''
       
