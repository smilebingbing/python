class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict={}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]]=1
            else:
                dict[nums[i]]+=1
        for x in dict:
            if dict[x]==1:
                return x
