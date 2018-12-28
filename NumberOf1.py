# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        flag = 1
        print(type(flag))
        count = 0
        # int 4字节，4x8=32位
        # python能表示任意大的数字，所以手动限定为32位
        maxBit = 32
        for i in range(maxBit):
            # &：按位与
            if n & flag:
                count += 1
            flag = flag << 1
        return count

solu = Solution()
print(solu.NumberOf1(3))


# 题目描述
# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示