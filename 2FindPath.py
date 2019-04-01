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
        if expectNumber == 0 and not root.left and not root.right:
            fg = True
            for i in range(0,len(self.liAll)-1):
                if len(self.li) > len(self.liAll[i]):
                    self.liAll.insert(i,self.li[:])
                    fg = False
            if fg or not self.liAll:
                self.liAll.append(self.li[:])
            print("run",fg,self.li,self.liAll)

        self.FindPath(root.left,expectNumber)
        self.FindPath(root.right,expectNumber)
        self.li.pop()
        return self.liAll

root = TreeNode(10)
node1 = TreeNode(5)
node2 = TreeNode(12)
node3 = TreeNode(4)
node4 = TreeNode(7)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
print(Solution().FindPath(root,22))
# 思路
# 1、首先需要有liAll和li两个全局变量，全局变量不需要作为递归函数findpath的参数，因此作为中间结果的li和liAll不会乱
# 2、在遍历不同路径时，很多路径之间都有很多公共的节点，如何利用公共节点，一是通过li这个栈来实现公共节点的值的重复利用
# 二是通过非尾递归，递归到左子树和右子树来实现节点位置的重复利用
