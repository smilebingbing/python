class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not len(nums):
            return
        par=len(nums)-2
        while par>=0 and nums[par]>=nums[par+1]:
            par-=1
        if par>=0:
            i=par+1
            while i<len(nums) and nums[i]>nums[par]:
                i+=1
            nums[par],nums[i-1]=nums[i-1],nums[par]
        left,right=par+1,len(nums)-1
        while left<=right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
