# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # not matrix[0]对应的情况是matrix=[[]]
        if not matrix or not matrix[0]:
            return None
        result=[]
        while(matrix):
            result += matrix.pop(0)
            if not matrix:
                break #if防止越界
            matrix = self.turn(matrix)
        return result

    # 逆时针旋转90度
    def turn(self,matrix):
        nrow=len(matrix)
        ncol=len(matrix[0])
        newMatrix=[]
        for i in range(ncol):
            sb=[]
            for j in range(nrow):
                sb.append(matrix[j][i]) #取矩阵的每列第i列
            newMatrix.append(sb)
        newMatrix.reverse()
        return newMatrix

# 题目描述
# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字

# 思路2 优化
# 思考发现每次转一圈的起始节点坐标都为（x,x）形式，且继续打印每一圈的循环条件是 2start < rows, 2start<cols
# 而每次打印一圈时分为打印行，列，行，列四个部分，每次打印的起始/终止行号/列号可以通过start以及rows,cols算出来
