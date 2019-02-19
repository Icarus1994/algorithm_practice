# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 先序遍历得到s
    def Serialize(self, root):
        # write code here
        if not root:
            return "#,"
        return str(root.val) + "," + self.Serialize(root.left) + self.Serialize(root.right)

    # 根据s通过先序遍历得到二叉树
    def Deserialize(self, s):
        # write code here
        return self.deserializeIteration(s)[0]

    def deserializeIteration(self,s):
        if not s:
            return None
        if s[0] == "#":
            return None,s[2:]
        else:
            i = 0
            while i< len(s) and s[i] != ",":
                i += 1
        node = TreeNode(int(s[:i]))
        node.left, s = self.deserializeIteration(s[i+1:])
        node.right, s = self.deserializeIteration(s)
        return node, s

root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

root.left = node1
root.right = node2
node1.left = node3
node1.right = node4

res = Solution().Serialize(TreeNode(3))
print(res)

des = Solution().Deserialize(res)
print(des.val)


# python l[i]和l[i:]报错和不报错
l = [1]
l[1:]
# print(l[1:])
# s = "342,"
# node = TreeNode(int(s[:3]))
# print(node,node.val)