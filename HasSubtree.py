# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def IsSameTree(self, r1, r2):
        if not r2: return True
        if (not r1) or r1.val != r2.val:
            return False
        return self.IsSameTree(r1.left,r2.left) and self.IsSameTree(r1.right, r2.right)

    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        if pRoot1.val == pRoot2.val:
            ans = self.IsSameTree(pRoot1,pRoot2)
            if ans:return True
        return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
