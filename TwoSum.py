class Solution(object):
    def twoSum(self,nums,target):
        D=dict()
        for x in range(len(nums)):
            D [nums[x]]=x
        for x in range(len(nums)):
            index1=x
            index2=D.get(target-nums[x])
            if index2:
                return index1,index2
#the second method
class Solution(object):
    def twoSum(self,nums,target):
        for i,value in enumerate(nums):
            if (target-value) in nums:
                index=nums.index(target-value)
                if i!=index:
                    if i<index:
                        return [i,index]
                    else:
                        return [index,i]

# the third method
class solution(object):
    def twoSum(self,nums,target):
        number=sorted(nums)
        length=len(nums)
        left=0
        right=length-1
        index=[]
        while left<right:
            sum=number[left]+number[right]
            if sum==target:
                for i in range(length):
                    if nums[i]==number[left]:
                        index.append(i)
                    elif nums[i]==number[right]:
                        index.append(i)
                    if len(index)==2:
                        break
                break
            elif sum<target:
                left+=1
            else:
                right-=1
        return index


            

            

            
       



                    