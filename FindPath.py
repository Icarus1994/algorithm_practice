# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        # 全局变量
        self.li = []
        self.liAll = []

    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return self.liAll
        self.li.append(root.val)
        expectNumber -= root.val
        if expectNumber==0 and not root.left and not root.right:
            self.liAll.append(self.li[:])
        self.FindPath(root.left,expectNumber)
        self.FindPath(root.right,expectNumber)
        self.li.pop()
        return self.liAll