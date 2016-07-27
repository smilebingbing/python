class Solution(object):
    def fourSum(self,nums,target):
        res=[]
        if len(nums)<4:
            return res
        nums.sort()
        i=0
        while i<len(nums)-3:
            j = i +1
            while j<len(nums)-2:
                k,x=j+1,len(nums)-1
                while k<x:
                    sum=nums[i]+nums[j]+nums[k]+nums[x]
                    if sum==target:
                        res.append([nums[i],nums[j],nums[k],nums[x]])
                        k+=1
                        x-=1
                        while k<x and nums[k]==nums[k-1]:
                            k+=1
                        while k<x and nums[x]==nums[x+1]:
                            x-=1
                    elif sum>target:
                        x-=1
                    else:
                        k+=1
                j+=1
                while j<len(nums)-1 and nums[j]==nums[j-1]:
                    j+=1
            i +=1
            while i<len(nums)-1 and nums[i]==nums[i-1]:
                i+=1
        return res
if __name__=='__main__':
    s=Solution()
    print (s.fourSum([0,1,0,0,7,0],8))

