# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if not root:
            return []
        return self.printTree([root],[])

    def printTree(self,thisRow, resultList):
        if not thisRow:
            return resultList
        nextRow = []
        for node in thisRow:
            resultList.append(node.val)
            if node.left:
                nextRow.append(node.left)
            if node.right:
                nextRow.append(node.right)
        print(resultList)
        print(nextRow)
        return self.printTree(nextRow,resultList)

# 题目描述
# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。
# 注意
# 对一个空列表使用append方法，得到的是[element],而不是[element,]形式的列表