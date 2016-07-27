class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        list1=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        list2=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        list=''
        for i in range(0,len(list1)):
            while num>=list1[i]:
                num-=list1[i]
                list+=list2[i]
        return list