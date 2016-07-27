class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        minlenstrs=9999
        index=0
        for i in range(0,len(strs)):
            if len(strs[i])<minlenstrs:
                minlenstrs=len(strs[i])
                index=i
        shortstrs=strs[index]
        list =[0 for i in range(len(shortstrs))]
        for i in range(0,len(shortstrs)):
            for j in range(0,len(strs)):
                if strs[j][i]==shortstrs[i]:
                    list[i]+=1
        prefix=''
        for i in range(0,len(shortstrs)):
            if list[i]==len(strs):
                prefix+=shortstrs[i]
            else:
                break
        return prefix
if __name__=='__main__':
    strs=["a","b"]
    print(Solution().longestCommonPrefix(strs))
            
                
