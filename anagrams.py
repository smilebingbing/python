class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict={}
        for s in strs:
            sort_s=''.join(sorted(s))
            if dict.get(sort_s):
                dict.get(sort_s).append(s)
            else:
                dict[sort_s]=[s]
        ret=[]
        for item in dict:
            ret.append(dict[item])
        return ret

"""
True
"""