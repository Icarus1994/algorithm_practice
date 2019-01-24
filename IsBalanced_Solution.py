# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsBalanced_Solution(self,pRoot):
        if not pRoot:
            return True
        if abs(self.findDepth(pRoot.left)-self.findDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def findDepth(self,node):
        if not node:
            return 0
        return max(self.findDepth(node.left),self.findDepth(node.right))+1
pRoot = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
pRoot.left = node2
pRoot.right = node3

node4 = TreeNode(4)
node5 = TreeNode(5)
node2.left =node4
node2.right = node5

node6 = TreeNode(6)
node3.right = node6

node7 = TreeNode(7)
node5.left = node7

solu = Solution()
result = solu.IsBalanced_Solution(pRoot)
print(result)