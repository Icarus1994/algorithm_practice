# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:
            return None
        if pNode.right:
            return self.middleOrderPrintFirstNode(pNode.right)
        else:
            while pNode.next and pNode is pNode.next.right:
                pNode = pNode.next
            return None if not pNode.next else pNode.next

    def middleOrderPrintFirstNode(self,node):
        return node if not node.left else self.middleOrderPrintFirstNode(node.left)

# 思路
# 分2种情况
# 1 将pNode视为一个子树的根节点，当该子树有右子树时肯定去遍历右子树找下一节点
# 2 pNode没有右子树，那么以pNode为根的子树已经遍历完了，将其视为整体，判断该子树在父节点中是左子节点还是右子节点
# 如果是右子树就说明以当前pNode节点的父节点father为根节点的子树也已经遍历完了，继续判断father在其父节点中是左子节点还是右子节点

# valueA if 条件1 else valueB
# A，B没有交集。如果当A或B时要结束循环，那么在全集中，应该当非A且非B时继续循环

