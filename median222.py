class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x=len(nums1)
        y=len(nums2)
        if x==0:
            if y%2==0:
                return (nums2[y//2-1]+nums2[y//2])/2.0
            else:
                return (nums2[y//2])
        if y==0:
            if x%2==0:
                return (nums1[x//2-1]+nums1[x//2])/2.0
            else:
                return (nums1[x//2])
        mid=(x+y+1)//2
        i=0
        j=0
        k=0
        midleft=0
        midright=0
        while k<mid:
            if nums1[i]<=nums2[j]:
                midleft=nums1[i]
                i+=1
                k+=1
            else:
                nums1[i]>nums2[j]
                midleft=nums2[j]
                j+=1
                k+=1
            if i>=x or j>=y:
                break
        if i<x and j<y:
            midright=min(nums1[i],nums2[j])
        elif i>=x:
            while k<mid:
                midleft=nums2[j]
                j+=1
                k+=1
            midright=nums2[j]
        else:
            while k<mid:
                midleft=nums1[i]
                i+=1
                k+=1
            midright=nums1[i]
        if (x+y)%2==0:
            return (midleft+midright)/2.0
        else:
            return midleft




                

            
