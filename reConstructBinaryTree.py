# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        # list.pop()复杂度为O(n)
        root = TreeNode(pre.pop(0))
        index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        return root
# 思路1 尾递归
# 原来给出的reConstructBinaryTree方法中不包含treeNode节点这一函数，
# 因此考虑再写一个包含节点对象参数的函数通过尾递归传递到下一个函数中
# 又因为递归函数收到节点后无法判断自己是作为左子树还是右子树继续执行，
# 因此需要递归到左子树和右子树的两个递归函数

# 思路2 非尾递归
