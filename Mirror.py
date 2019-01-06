# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def reverseLeftAndRight(self,node):
        if not node:
            return
        tmp = node.right
        node.right = node.left
        node.left = tmp
        self.reverseLeftAndRight(node.left)
        self.reverseLeftAndRight(node.right)

    def Mirror(self, root):
        # write code here
        if not root:
            return root
        tmp = root.right
        root.right = root.left
        root.left = tmp
        nRoot = root
        self.reverseLeftAndRight(root.left)
        self.reverseLeftAndRight(root.right)
        return nRoot

# 题目描述
# 操作给定的二叉树，将其变换为源二叉树的镜像。