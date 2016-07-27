class Solution(object):
    def removeDuplicates(self, nums):
        label=0
        i=0
        while i<len(nums):
            nums[label]=nums[i]
            label+=1
            i+=1
            if i<len(nums) and nums[i]==nums[i-1]:
                nums[label]=nums[i]
                label+=1
            while i<len(nums) and nums[i]==nums[i-1]:
                i+=1
        return label
        """
        :type nums: List[int]
        :rtype: int
        """
if __name__=='__main__':
    s=Solution()
    print (s.removeDuplicates([1,1,2,2,2,2]))
