class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(n-i):
                matrix[i][j],matrix[n-1-j][n-1-i]=matrix[n-1-j][n-1-i],matrix[i][j]
        for i in range(n/2):
            for j in range(n):
                matrix[i][j],matrix[n-1-i][j]=matrix[n-1-i][j],matrix[i][j]

'''
1.第一种方法： 先沿副对角线翻转，再沿水平中线进行翻转

2.第二种方法： 先沿水平中线翻转，再沿主对角线进行翻转


'''
class Solution(0bject):
    def rotate(self,matrix):
        matrix[:]=zip(*[::-1])
        return matrix