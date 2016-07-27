class Solution(object):
    def lengthOfLastWord(self,s):
        word=s.split()
        if word:
            return len(word[-1])
        else:
            return 0