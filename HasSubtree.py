# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def DoesTree1HaveTree2(self, pRoot1, pRoot2):
        # 根据下行代码可知当pRoot2为空而pRoot1不为空时可以认为树B是树A的子结构
        # not pRoot2包括仅仅pRoot2为空和pRoot1以及pRoot2同时为空的情况
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1HaveTree2(pRoot1.left, pRoot2.left) and \
               self.DoesTree1HaveTree2(pRoot1.right,pRoot2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        result = False
        # 因为hasSutree中有递归，所以If语句会被重复调用
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1HaveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

# 题目描述
# 输入两棵二叉树A，B，判断B是不是A的子结构（约定空树不是任意一个树的子结构）。

# 思路
# 问题可用回溯法解决，因此考虑用递归的方式写出