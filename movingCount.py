# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.step = 0
        self.matrix = []
        self.threshold = 0
        self.row = 0
        self.col = 0

    def movingCount(self, threshold, rows, cols):
        # write code here
        if threshold <= 0:
            return 0
        # 考虑行列为0
        self.threshold = threshold
        self.row = rows
        self.col = cols
        self.matrix = [False for i in range(rows * cols)]
        self.iterationMoving(0,0)
        return self.step

    def iterationMoving(self,x,y):
        if 0 <= x < self.row and 0 <= y < self.col and \
                self.count(x)+self.count(y) <= self.threshold\
                and not self.matrix[x * self.col + y]:
            print(x,y)
            self.step += 1
            self.matrix[x * self.col + y] = True
            self.iterationMoving(x+1,y)
            self.iterationMoving(x,y+1)
            self.iterationMoving(x-1,y)
            self.iterationMoving(x,y-1)

    def count(self, num):
        cnt = 0
        while num>0:
            cnt += num % 10
            num //= 10
        return cnt
# 27ms,5720k
res = Solution().movingCount(3,0,0)
print(res)
