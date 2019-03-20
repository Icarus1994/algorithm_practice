# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        # 规律：f(n) = 2^(n-1)
        return 2**(number-1)


# 题目描述
# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
# 求该青蛙跳上一个n级的台阶总共有多少种跳法

# 思路
# 参照跳台阶的题，f(n) = f(n-1) + f(n-2) + ... + f(1)
# 等比数列f(n) = a1*k^(n-1)
