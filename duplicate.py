# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        if not numbers:
            return False
        fg = False
        length = len(numbers)
        for i in range(len(numbers)):
            index = numbers[i]
            if numbers[i] >= length:
                index -= length
            if numbers[index] >= length:
                fg = True
                duplication[0] = index
                break
            else:
                numbers[index] += length
        print(duplication[0])
        return fg
num = [2,3,1,0,2,5,3]
dup = [-1]
result = Solution().duplicate(num,dup)
print(result)

# 注意
# 题目中说的找到任意重复的一个值并赋值到duplication[0]，其实duplication[0]没有什么影响，
# 换成复制给一个变量a也是一样的，不需要讲所有重复的值都放到duplication这个list中

# 思路
# 充分利用数组数值都在0~n-1之间（也即在数组下标之内）的特点，对于出现过的数字val，
# 在num[val]上设置加n,从而当遍历到num[val]时根据值知道已经重复，根据下标val知道是哪个值已经重复了