class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len ,nums2_len = len(nums1) , len(nums2)

        target = (nums1_len+nums2_len+1)//2
        i  = 0
        p_1 ,p_2 = 0,0 #两个游标
        ans = 0
        ans2 = 0

        while i < target :
            if nums1[p_1]<=nums2[p_2]:
                ans = nums1[p_1]
                p_1+=1
                i+=1
            else:
                nums1[p_1]>nums2[p_2]
                ans = nums2[p_2]
                p_2+=1
                i+=1
            if p_1 >=nums1_len or p_2>=nums2_len :
                break

        if p_1< nums1_len and p_2 < nums2_len :  # 均未越界
            ans2 = min (nums1[p_1],nums2[p_2])
        elif p_1 >=nums1_len :
            while i < target+1:
                p_1+=1 
            ans = nums1[p_1]
            ans2 = nums1[p_1]
        else :
            while i < target+1:
                p_2+=1 
            ans = nums2[p_2]
            ans2 = nums2[p_2]

        if (nums1_len+nums2_len)%2 == 0 :
            return ans
        else :
            return (ans+ans2)/2
