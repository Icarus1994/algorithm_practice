# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        # listTail指向排序后位于当前节点左边的节点
        # listHead指向头节点
        self.listHead = None
        self.listTail = None

    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return
        self.Convert(pRootOfTree.left)
        if self.listHead == None:
            self.listHead = pRootOfTree
            self.listTail = pRootOfTree
        else:
            self.listTail.right = pRootOfTree
            pRootOfTree.left = self.listTail
            self.listTail = pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.listHead

# 算法理解
# 二叉搜索树，按照中序遍历，每次打印树的根节点（叶子节点也是根节点），就会得到一个有序列表
# 因此可设置listTail,每次记录被遍历到的根节点，改变前一节点（即listTail）和当前根节点的指针，
# 一直到所有节点作为根节点被遍历完
# 因为每次只改变前一节点和当前根节点之间的指向关系，因此不会对之后的遍历节点造成影响