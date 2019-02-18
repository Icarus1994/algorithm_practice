# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot or (not pRoot.left and not pRoot.right):
            return True
        if not pRoot.left or not pRoot.right:
            return False
        else:
            leftSubTree = [pRoot.left]
            rightSubTree = [pRoot.right]
            while leftSubTree and rightSubTree:
                if not leftSubTree[0] and not rightSubTree[0]:
                    leftSubTree.pop(0)
                    rightSubTree.pop(0)
                elif leftSubTree[0] and rightSubTree[0] and leftSubTree[0].val == rightSubTree[0].val:
                    leftSubTree.append(leftSubTree[0].left)
                    leftSubTree.append(leftSubTree[0].right)
                    leftSubTree.pop(0)
                    # 注意右子树append节点的顺序与左子树的相反
                    rightSubTree.append(rightSubTree[0].right)
                    rightSubTree.append(rightSubTree[0].left)
                    rightSubTree.pop(0)
                else:
                    return False
            return False if (leftSubTree or rightSubTree) else True

root = TreeNode(8)
node1 = TreeNode(6)
node2 = TreeNode(6)
node3 = TreeNode(5)
node4 = TreeNode(7)
node5 = TreeNode(7)
node6 = TreeNode(5)

root.left = node1
root.right = node2

node1.left = node3
node1.right = None
node2.left = None
node2.right = node6
res = Solution().isSymmetrical(root)
print(res)

# 思路1 非递归
# 二叉树要对称，那么对于左子树和右子树，每一层上的值存入List中也应该是对称的
# 但这里要注意的一点是，如果一层中有的位置上没有节点则要用None代替，避免值顺序相同位置却不一样的情况
# 当然某一层的"None"节点到下一层不必再存入为两个None了
# 和递归思路比多了两个List的空间复杂度，但是递归压栈要空间，可能各有优势吧（没仔细分析）

# 思路2 递归比较左右子树
# 参考讨论区








