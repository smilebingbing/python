class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==None or needle==None:
            return -1
        len_h=len(haystack)
        len_n=len(needle)
        i=0
        for i in range(len_h-len_n+1):
            j=0
            k=i
            while j<len_n:
                if haystack[k]==needle[j]:
                    j+=1
                    k+=1
                else:
                    i+=1
                    break
            if len_n==j:
                return i
        return -1
'''
correct
暴力破解法
'''