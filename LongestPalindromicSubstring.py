class Solution(object):
    def getlongest(self,s,l,r):
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome=""
        for i in range(len(s)):
            tmp=self.getlongest(s,i,i)
            if len(tmp)>len(palindrome):
                palindrome=tmp
            tmp=self.getlongest(s,i,i+1)
            if tmp>len(palindrome):
                palindrome=tmp
        return palindrome
"""
false
"""
     
