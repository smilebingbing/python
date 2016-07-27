class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rownum=len(matrix)
        column=len(matrix[0])
        row=[False for i in range(rownum)]
        col=[False for i in range(column)]
        for i in range(rownum):
            for j in range(column):
                if matrix[i][j]==0:
                    row[i]=True
                    col[j]=True
        for i in range(rownum):
            for j in range(column):
                if row[i] or col[j]:
                    matrix[i][j]=0