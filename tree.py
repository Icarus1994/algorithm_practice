# -*- coding:utf-8 -*-
def printTree(treeNode):
    if treeNode == None:
        return
    print(treeNode.val,'\n')
    printTree(treeNode.left)
    printTree(treeNode.right)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def setLeft(self,left):
        self.left = left

    def setRight(self,right):
        self.right = right

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        leftTreeLen = -1
        if len(pre)==0:
            return None
        elif len(pre) == 1:
            return TreeNode(pre[0])
        else:
            node = TreeNode(pre[0])
            for i in range(len(tin)):
                if tin[i] == pre[0]:
                    leftTreeLen = i
                    # rightTreeLen = len(tin-i)
                    break
            if leftTreeLen == -1:
                return None
            node.setLeft(self.reConstructBinaryTree(pre[1:leftTreeLen+1],tin[0:leftTreeLen]))
            node.setRight(self.reConstructBinaryTree(pre[leftTreeLen+1:],tin[leftTreeLen+1:]))
        return node


pre = [1,2,4,7,3,5,6,8]
tin = [4,7,2,1,5,3,8,6]
solu = Solution()
# print(solu.reConstructBinaryTree(pre,tin).val)
treeNode = solu.reConstructBinaryTree(pre,tin)
printTree(treeNode)

# 本题中不用考虑给的数据前序遍历和中序遍历无法构成一棵树的情况




