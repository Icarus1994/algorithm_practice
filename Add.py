# -*- coding:utf-8 -*-
class Solution:
    def Add(self, a, b):
        # a是a+b不进位的结果，b是a+b进位的结果
        while (b):
            a, b = (a ^ b) & 0xFFFFFFFF, ((a & b) << 1) & 0xFFFFFFFF

        print(a ^ 0xFFFFFFFF)
        return a if a <= 0x7FFFFFFF else ~(a ^ 0xFFFFFFFF)
# 循环中假设32位字长时不会溢出
# a ^ 0xFFFFFFFF将a限制在了32位
# 最后当a为负数时使用~(a^0xFFFFFFFF)最终结果是让a = a-1
# 其中a^0xFFFFFFFF可以让a限制在32位，~x = -x-1
print(~(-5))
result = Solution().Add(5,-10)
