# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        cnt = 0
        for i in range(1, n + 1):
            for letter in str(i):
                if letter == "1":
                    cnt += 1
        return cnt
# 注意
# 不用把问题想复杂，遍历即可，因为整数不可能无限大，复杂度也就是O(n)