class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start=0
        end=len(s)-1
        while start<end:
            while start<end and not s[start].isalpha() and not s[start].isdigit():
                start+=1
            while start<end and not s[end].isalpha() and not s[end].isdigit():
                end-=1
            if start<end and s[start].lower()!=s[end].lower():
                return False
            else:
                start+=1
                end-=1
        return True
'''
correct
'''