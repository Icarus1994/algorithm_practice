# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.col = None
        self.row = None
        self.b = True

    def hasPath(self, board, row, col, word):
        self.col, self.row = col, row
        # 为什么还要加list，本身不就是二重list吗
        board = [list(board[col * i:col * i + col]) for i in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    self.b = False
                    self.search(board, word[1:], [(i, j)], i, j)
                    if self.b:
                        return True
        return False

    def search(self, board, word, list, i, j):
        if word == "":
            self.b = True
            return
        if j != 0 and (i, j - 1) not in list and board[i][j - 1] == word[0]:
            self.search(board, word[1:], list + [(i, j - 1)], i, j - 1)
        if i != 0 and (i - 1, j) not in list and board[i - 1][j] == word[0]:
            self.search(board, word[1:], list + [(i - 1, j)], i - 1, j)
        if j != self.col - 1 and (i, j + 1) not in list and board[i][j + 1] == word[0]:
            self.search(board, word[1:], list + [(i, j + 1)], i, j + 1)
        if i != self.row - 1 and (i + 1, j) not in list and board[i + 1][j] == word[0]:
            self.search(board, word[1:], list + [(i + 1, j)], i + 1, j)
# 思路
# 遍历寻找匹配的path中第一个字符
# 之后通过递归来推进path字符的遍历
# 通过if语句来选择周围的下一个字符
# list来存储是否使用过matrix中某字符