# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i, s in enumerate(matrix):
            if s == path[0] and self.visit([(i // cols, i % cols)], matrix, rows, cols, path):
                return True
        return False

    def visit(self, ans, matrix, rows, cols, path):
        if len(ans) == len(path):
            return True
        i, j = ans[-1]
        nex = [(ii, jj) for ii, jj in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]
               if 0 <= ii < rows and 0 <= jj < cols and
                # 将已经匹配过的字符的下标而不是字符本身放到ans中，从而可以判断该字符是否被使用过
               (ii, jj) not in ans and
                # 每次执行时用ans长度标识在path中匹配字符的位置
               matrix[ii * cols + jj] == path[len(ans)]]
        # sum里的list中的每个值(T or F)都代表的是一次完整的探索，要么找到一个完整的路径返回True,
        # 要么因为ans[-1]周围合适的值不存在而停止
        # 缺点：当已经发现一条完整路径后还是会继续执行下一行
        return sum([self.visit(ans + [x], matrix, rows, cols, path) for x in nex])

l = [3,True,False]
print(sum(l))

