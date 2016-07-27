class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        L=[]
        for i in range(2**n):
            return L.append((i>>1)^i)

```
1. 自然二进制码转换为格雷码：保留自然二进制码的最高位作为格雷码的最高位，格雷码次高位为二进制码的高位与次高位异或，其余各位与次高位的求法类似。
2. 格雷码转换为二进制码：保留格雷码的最高位作为自然二进制码的最高位，次高位为自然二进制码高位与格雷码次高位异或，其余各位与次高位的求法类似。
问题：生成n比特的所有格雷码
方法：利用数学公式，对从0-2**n-1的所有整数，转化为格雷码
```