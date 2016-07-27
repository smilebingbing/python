class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r=[]
        if len(nums)<3:
            return r
        nums=sorted(nums)
        i=0
        while i<len(nums):
            j,k=i+1,len(nums)-1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==0:
                    r.append([nums[i],nums[j],nums[k]])
                    return r
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif sum>0:
                    k-=1
                else:
                    j+=1
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            i+=1
        return r

'''
#the second method
class Solution(object):
    def threeSum(self,num):
        num.sort()
        res=[]
        for i in range(len(num)-2):
            if i==0 or num[i]>num[i-1]:
                left=i+1
                right=len(num)-1
                while left<right:
                    if num[left]+num[right]==-num[i]:
                        res.append([num[i],num[left],num[right]])
                        left+=1
                        right-=1
                        while left<right and num[left]==num[left-1]:
                            left+=1
                        while left<right and num[right]==num[right+1]:
                            right-=1
                    elif num[left]+num[right]<-num[i]:
                        while left<right:
                            left+=1
                            if num[left]>num[left-1]:
                                break
                    else:
                        while left<right:
                            right-=1
                            if num[right]<num[right+1]:
                                break
        return res
'''
if __name__=='__main__':
    s=Solution()
    print(s.threeSum([0,0,0]))




                           

                    

                

               
