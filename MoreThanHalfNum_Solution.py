# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        dict ={}
        length = len(numbers)/2
        for i in numbers:
            dict[i] = 0
        for i in numbers:
            dict[i] += 1
            if dict[i] > length:
                return i
        return 0
# 添加或修改字典元素
dict = {}
dict[3] = 1
# line8中len因为在赋值语句等号右边已经存在，因此等号左边变量不能起同样的名称"len",否则会报错
