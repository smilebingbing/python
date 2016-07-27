class Solution(object):
    def removeElement(self,nums,target):
        label=0
        for i in range(len(nums)):
            if nums[i]!=target:
                nums[label]=nums[i]
                label+=1
        return label