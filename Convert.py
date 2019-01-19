# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.list = []

    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return None
        elif not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree
        self.getSortedList(pRootOfTree)
        for i in range(0,len(self.list)-1):
            self.list[i].right = self.list[i+1]
            self.list[i+1].left = self.list[i]
        return self.list[0]
    # 先序遍历，将结果保存到list中
    # 链表题如果要返回头指针都可以通过保存到list中，处理后返回list[0]
    def getSortedList(self,node):
        if not node:
            return
        self.getSortedList(node.left)
        self.list.append(node)
        self.getSortedList(node.right)
# 题目
# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。
# 要求不能创建任何新的结点，只能调整树中结点指针的指向。