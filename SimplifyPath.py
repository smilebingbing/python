class Solution(object):
    def simplifyPath(self,path):
        stack=[]
        for i in path.split('/'):
            if i in ('','.'):
                pass
            elif i=='..':
                if stack:stack.pop()
            else:
                stack.append(i)
        return '/'+'/'.join(stack)