# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if not matrix or matrix == []:
            return []
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return [matrix[0][0]]
        row = len(matrix)
        col = len(matrix[0])
        start, ans = 0,[]
        while start * 2 < row and start * 2 < col:
            ans += self.rotatePrit(row,col,start,matrix)
            start += 1
        return ans

    def rotatePrit(self, row, col, start,matrix):
        # endX,endY位置都是需要打印的
        endX = row - start - 1
        endY = col - start - 1
        ans = []
        for i in range(start,endY + 1):
            ans.append(matrix[start][i])

        if start < endX:
            for i in range(start+1,endX+1):
                ans.append(matrix[i][endY])

        if start < endX and start < endY:
            for i in range(endY-1,start-1,-1):
                ans.append(matrix[endX][i])
        if start < endY and endX-1 > start:
            for i in range(endX-1,start,-1):
                ans.append(matrix[i][start])
        return ans

matrix = [[1],[4],[6],[8],[10]]
ans = Solution().printMatrix(matrix)
print(ans)

# 题目描述
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字

# 思路
# 1、每次打印一圈的起始节点坐标都为（x,x）形式，起始节点(x,x)应满足2x<col && 2x<row
# 2、打印一圈时，分为从左到右，从上到下，从右到左，从下到上四步，想象有四个宽度为1的长方形，每一步都走到可以打印的尽头
# 通过start,endX,endY就可以确定要打印的这一圈的边界，而endX,endY可以通过start来确定
# 难点
# 判断四个方向是否打印的边界条件
