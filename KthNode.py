# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot:
            return None
        self.arr = []
        self.middleOrder(pRoot)
        return self.arr[k-1] if 0 < k <= len(self.arr) else None

    def middleOrder(self,node):
        if not node: return
        self.middleOrder(node.left)
        self.arr.append(node)
        self.middleOrder(node.right)


# 思路
# 利用对二叉搜索树的特点进行中序遍历，可以得到按大小顺序排列的一组节点
