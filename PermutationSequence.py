class Solution(object):
    def getPermutation(self,n,k):
        result=' '
        k-=1
        fac=1
        for i in range(1,n):
            fac*=i
        num=[1,2,3,4,5,6,7,8,9]
        for i in reversed(range(n)):
            a=num[k/fac]
            result+=str(a)
            num.remove(a)
            if i!=0:
                k%=fac
                fac/=i
        return result




'''
问题：求全排列的第K个序列
思路：判断第K个序列的第一位到第N位的数字，
      首先判断第一位的数字，使用倒推法，它的组合数不能超过K的值

1. 第一位的数字=K/(n-1)!   ,使用for循环计算(n-1)!
2. 计算出来的数字向上取整，然后把数字变成字符串形式，添加到结果中
3. 在九个数字中，将已经确定的数字移除
4. 逆序遍历n，k=k%fac
            fac=fac/i
    i!=0,循环，

'''