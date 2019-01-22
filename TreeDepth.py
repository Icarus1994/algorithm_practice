# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.path = 0
        self.depth = 0

    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        self.path += 1
        if not pRoot.left and not pRoot.right:
            if self.path > self.depth:
                self.depth = self.path
        self.TreeDepth(pRoot.left)
        self.TreeDepth(pRoot.right)
        self.path -= 1
        return self.depth


pRoot = TreeNode(3)
left = TreeNode(4)
right = TreeNode(5)
gradeSun = TreeNode(8)
right.right = gradeSun
pRoot.left = left
pRoot.right = right
result = Solution().TreeDepth(pRoot)
print(result)

# 题目描述
# 输入一棵二叉树，求该树的深度。
# 从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。

# 思路
# 和之前求"二叉树中和为某一路径的值"思路一样
# 特点是（1）通过递归函数返回上一级节点，（2）通过全局变量存储路径长度path和树的深度depth