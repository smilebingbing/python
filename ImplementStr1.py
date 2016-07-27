class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_h=len(haystack)
        len_n=len(needle)
        for i in range(len_h-len_n+1):
            if haystack[i:i+len_n]==needle:
                return i
        return -1