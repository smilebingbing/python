class  Solution(object):
    def ThreeSumClosest(self,num,target):
        if len(num)<3:
            return num
        ret=num[0]+num[1]+num[2]
        num.sort()
        i=0
        for i in range(len(num)):
            left=i+1
            right=len(num)-1
            while left<right:
                sum=num[i]+num[left]+num[right]
                if abs(sum-target)<abs(ret-target):
                    ret=sum
                if ret>target:
                    right-=1
                elif ret<target:
                    left+=1
                else:
                    #left+=1
                    #right-=1
        return ret

if __name__=='__main__':
    s=Solution()
    print (s.ThreeSumClosest([0,0,1],1))


"""
1. 先设置一个初始值，假设为前三个数之和
2. 对列表进行排序，i从零开始循环，left=i+1,right=最后一个值
3. 令sum=它们三个之和，然后sum和ret分别与目标值进行比较，用绝对值函数，用ret标记较小的值
4. 
"""