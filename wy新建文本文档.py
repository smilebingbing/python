
"""
S3:
    1.首先获取两个长度 len1  len2
    2. 设置两个游标 p1 p2 
    3. 奇偶数，总数为奇数，找到一个ans 返回， 总数偶数继续找下一个ans2  返回平均

T： 
    1. 判断一个为空串，此时直接返回另一个medain
    2. while  时 防止越界，当一个越界后跳出 while, 继续寻找ans

"""
class Solution3(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1_len ,nums2_len = len(nums1) , len(nums2)
        #  当其中一个为空串时 ，直接返回medain(判断总数奇偶)
        if nums1_len == 0: 
            if (nums2_len)%2 == 0 :
                return (nums2[nums2_len//2-1]+nums2[nums2_len//2])/2.0
            else :
                return nums2[nums2_len//2]
        if nums2_len == 0: 
            if (nums1_len)%2 == 0 :
                return (nums1[nums1_len//2-1]+nums1[nums1_len//2])/2.0
            else :
                return nums1[nums1_len//2]

        # target 最终找第target 个数字， 如果和为偶数个  则还需找下一个
        target = (nums1_len+nums2_len+1)//2
        i  = 0
        p_1 ,p_2 = 0,0 #num1 num2 的两个游标
        # ans 记录第target 个数字， ans2 记录第target+1 个数字
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
        
        # 跳出while 时，已经找到ans, 
        if p_1< nums1_len and p_2 < nums2_len :  # 均未越界
            ans2 = min (nums1[p_1],nums2[p_2])
        # nums1  游标越界，
        elif p_1 >=nums1_len :
            while i < target:
                ans = nums2[p_2]
                p_2+=1 
                i+=1
            ans2 = nums2[p_2]
        else :
            while i < target:
                ans = nums1[p_1]
                p_1+=1 
                i+=1
            ans2 = nums1[p_1]

        if (nums1_len+nums2_len)%2 == 0 :
            return (ans+ans2)/2.0
        else :
            return ans