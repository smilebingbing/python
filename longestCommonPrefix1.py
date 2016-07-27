class Solution(object):
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        for i in range(0,len(strs[0])):
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[0][i]:
                    return strs[0][0:i]
        return strs[0]

if __name__=='__main__':
    strs=["aa","a"]
    print(Solution().longestCommonPrefix1(strs))

'''
    def longestCommonPrefix(self,strs):
        if len(strs)==0:
            return ""
        right=len(strs[0])-1
        for i in range(1,len(strs)):
            for j in range(0,right):
                if strs[i][j]!=strs[0][j]:
                    right=j-1
        return strs[0][0:right+1]
'''

'''
False :11 and 22 string index out of range
'''