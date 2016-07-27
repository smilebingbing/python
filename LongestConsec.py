class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        nums.sort()
        count=1
        ans=1
        i=0
        for i in range(length):
            if nums[i]-1==nums[i-1]:
                count+=1
            elif nums[i]-1>nums[i-1]:
                ans = max(ans,count)
                count=1
            else:
                pass
            i+=1
        return max(ans,count)
        



'''
1. 先对原序列排序，然后遍历一次找最长连续序列，
   时间复杂度是O(n*logn)*O(n)=O(n*log(n))
2. 而本题的复杂度要求是O(n)
'''