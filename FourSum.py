class Solution(object):
    def fourSum(self,num,target):
        res=[]
        if len(num)<4:
            return res
        num.sort()
        i=0
        while i<len(num)-3:
            j = i +1
            while j<len(num)-2:
                k,x=j+1,len(num)-1
                while k<x:
                    sum=num[i]+num[j]+num[k]+num[x]
                    if sum==target:
                        res.append([num[i],num[j],num[k],num[x]])
                        k+=1
                        x-=1
                        while k<x and num[k]==num[k-1]:
                            k+=1
                        while k<x and num[x]==num[x+1]:
                            x-=1
                    elif sum>target:
                        x-=1
                    else:
                        k+=1
                while j<len(num)-2 and num[j]==num[j+1]:
                    j+=1
            while i<len(num)-3 and num[i]==num[i+1]:
                i+=1
        return res
if __name__=='__main__':
    s=Solution()
    print (s.fourSum([0,1,0,0,7,0],8))



'''
1. 先排序
2. 确定最外层循环i，第二层循环j=i+1，然后剩下的选取一左一右，进行循环
3. 求四个数之和，然后和目标值进行比较，
4. 相等的时候，用一个值来记录一下，然后接着循环，去掉重复的值

'''

