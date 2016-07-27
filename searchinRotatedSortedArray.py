class Solution(object):
    def search(self,nums,target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)/2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left]<=target and target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            elif nums[mid]<nums[right]:
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1



'''
1. 二分查找进行搜索，时间复杂度为O(logn),直接遍历查找，时间复杂度为O(n)
2. 第一种是中间点之前是有序的，
   如果目标值大于左侧值小于中间值，那么让right=mid-1
   否则让left=mid+1
3. 第二种，中间点之前是无序的，
   如果目标值大于中间值小于右侧值，则left=mid+1
   否则right=mid-1

'''



