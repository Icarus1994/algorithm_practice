# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        arr = [pRoot]
        res = []
        while arr:
            i = len(arr)
            tmp = []
            while i > 0:
                if arr[0].left:
                    arr.append(arr[0].left)
                if arr[0].right:
                    arr.append(arr[0].right)
                tmp.append(arr.pop(0).val)
                i -= 1
            res.append(tmp)
        return res
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

res = Solution().Print(root)
for i in res:
    print(i)