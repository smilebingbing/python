class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==None:
            return -1
        next_val=self.Next(needle)
        i=0
        j=0
        while i<len(haystack) and j<len(needle):
            if j==-1 or haystack[i]==needle[j]:
                i+=1
                j+=1
            else:
                j=next_val[j]

        if j==len(needle):
            return i-j
        else:
            return -1

        