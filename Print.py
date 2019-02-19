# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        arr = [pRoot]
        fg = True
        res = []
        while arr:
            i = len(arr)
            tmp = []
            while i>0:
                if arr[0].left:
                    arr.append(arr[0].left)
                if arr[0].right:
                    arr.append(arr[0].right)
                tmp.append(arr.pop(0).val)
                i -= 1
            if not fg:
                tmp.reverse()
            res.append(tmp)
            fg = not fg
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
node2.left = node5
node2.right = node6
node6.right = node4

res = Solution().Print(TreeNode(3))
for i in res:
    print(i.val)

# 思路
# 使用队列对树按层序遍历，遍历过程中设置i计算每层含有的节点数量，
# 同一层的节点存入到临时数组tmp中，tmp根据当前层的位置决定是否反转，然后连接到最终结果数组arr中

# i表示每层节点数量，每次i减小到0后，此时arr的长度就是下一层节点的数量i
# fg指示本层节点打印顺序正反
# 树层序遍历时，arr每一层遍历的顺序不能变，因为变了之后下下层的顺序又有问题

# 本来想每次arr弹出第一个元素时append到res末尾或者insert到倒数第k个位置，但
# 问题：fg=False时,insert方法没法插入到最后一个元素，但是每次判断是不是本层第一个元素又比较麻烦
# 干脆加一个tmp，每取好一行的变量再extend到res



