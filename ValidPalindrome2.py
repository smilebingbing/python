class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s==' ':
            return True
        else:
            stmp=''
            for i in range(len(s)-1):
                if s[i]>='a' and s[i]<='z' or s[i]>='A' and s[i]<='Z':
                    stmp+=s[i]
            stmp=stmp.lower()
            for i in range(len(stmp)/2):
                if stmp[i]!=stmp[len(stmp)-1-i]:
                    return False
            return True