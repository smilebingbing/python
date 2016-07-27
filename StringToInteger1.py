class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        if str=='':
            return 0
        sum=0
        sign=1
        i=0
        length=len(str)
        int_max=2**31-1
        int_min=-(2**31)
        if str[i]=='+':
            i+=1
        elif str[i]=='-':
            i+=1
            sign=-1
        for i in range(i,length):
            if str[i]<'0' or str[i]>'9':
                break
            sum=sum*10+int(str[i])
            if sum>sys.maxint:
                break
        sum=sum*sign
        if sum>int_max:
            return int_max
        if sum<int_min:
            return int_min
        return sum


if __name__ == "__main__":
    s = Solution()
    ss = s.myAtoi("+")
    print(ss)  