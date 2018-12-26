# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number ==0:
            return 0
        k = number / 2 + 1
        sum = 0
        for i in range(int(k)):
            sum += self.combinations(number - i, i)
        return sum

    def combinations(self, n, k):
        deno = 1
        for i in range(n - k + 1, n + 1):
            deno *= i
        return int(deno / self.jieCheng(k))

    def jieCheng(self, n):
        outcome = 1
        for i in range(1, n + 1):
            outcome *= i
        return outcome
solu = Solution()
print(solu.rectCover(3))
# 题目描述
# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
# 请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

# 归结起来和跳台阶是一类问题