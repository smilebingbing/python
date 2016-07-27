class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s='1'
        for i in range(2,n+1):
            s=self.count(s)
        return s
    def count(self,s):
        t=''
        count=0
        cur='#'
        for i in s:
            if i!=cur:
                if cur!='#':
                    t+=str(count)+cur
                count=1
                cur=i
            else:
                count+=1
        t+=str(count)+cur
        return t
      