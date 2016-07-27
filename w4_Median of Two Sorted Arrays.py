# Error
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n1_left , n2_left = 0,0
        n1_right,n2_right = len(nums1)-1 , len(nums2)-1
        n1_mid ,n2_mid = 0,0

        while n1_left < n1_right :
            n1_mid  = (n1_left+n1_right)//2
            n2_mid  = (n2_left+n2_right)//2
            if nums1[n1_mid] == nums2[n2_mid] :
                return nums1[n1_mid]
            elif nums1[n1_mid] < nums2[n2_mid] :
                n1_left = n1_mid+1
                n2_right = n2_mid-1
            else :
                n1_right = n1_mid-1
                n2_left = n2_mid+1

        return (nums1[n1_left]+nums2[n2_left])/2



"""
Error : 奇偶数问题，思路与A2 类似，只是奇偶数判断error

"""





class Solution2 (object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l_num1 ,l_num2 = len(nums1) , len(nums2)
        # nums1始终指向较短序列，防止划分时 导致另一个 越界
        if l_num1 > l_num2 :
            l_num1,l_num2,nums1,nums2 = l_num2,l_num1,nums2,nums1
        # 在较短的序列上，滑动切分位置。min max  二分选择切分位置。
        s1_min , s1_max = 0,l_num1    # 标记S1_seg 范围，
        s1_seg , s2_seg = 0,0

        while s1_min<=s1_max:
            s1_seg = (s1_min+s1_max)//2  #找S1分割位置。
            s2_seg = (l_num1+l_num2+1)//2 - s1_seg  # 两个分割位置左边数目总共为总数一半(和为偶数)，或者多一个(奇)

            # 首先判断防止越界。 当> 时 表示 s1_seg 应该向左，左右移动max
            if s1_seg>0 and s2_seg<l_num2 and nums1[s1_seg-1] > nums2[s2_seg] :
                s1_max = s1_seg-1
            # s1_seg  应该向左
            elif s2_seg>0 and s1_seg<l_num1 and  nums2[s2_seg-1] > nums1[s1_seg]:
                s1_min = s1_seg+1
i
            else:
                # 首先找到左边的最大值
                if s1_seg == 0:
                     max_left  = nums2[s2_seg-1]
                elif s2_seg ==0:    #此处必须判断 防止[1][2]  
                    max_left = nums1[s1_seg-1]
                else :
                    max_left = max(nums1[s1_seg-1],nums2[s2_seg-1])
                # 当左侧已经判断完毕， 如果odd 没必要判断右边
                if (l_num1+l_num2)%2 : #odd
                    return max_left
                if s1_seg == l_num1:
                    min_right  = nums2[s2_seg]
                elif s2_seg == l_num2:
                    min_right = nums1[s1_seg]
                else :
                    min_right = min(nums1[s1_seg],nums2[s2_seg])
                return (max_left+min_right)/2.0



"""
A2核心思想：

1. 对AB 数组找到合适的ij 将AB 分为左右两半。(左边全部小于右边)
2. 关于奇偶数：不单独考虑，只考虑总和，总和为奇：左边部分max; 总和为偶： 左边max 和右边min 均值。
3. 我们只需移动i 即可。对i 使用二分 移动i。依次缩小i范围。
4. i 应该在较短的一个数组移动，防止j 越界。
5. 移动i时候应该判断 防止越界。
6. 只要改变i+j 和 即可 变为top k 问题


"""




"""
A3 :  也可以将此问题转化为求top k 问题。 对于total为奇数和偶数 分别处理即可。

    top k 的求法可以使用二分 递归求。 为知笔记

Q ： python 如何同C 一样 list 传递部分片段，不使用切片？
"""





if __name__ == '__main__':
    S =Solution2()
    ss =S.findMedianSortedArrays([1],[2])
    print(ss)


"""
Q :   两个有序数组 a1 a2  找到medain.   复杂度：O (log (m+n)).

"""        