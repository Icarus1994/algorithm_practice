# -*- coding:utf-8 -*-
import itertools
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        res = itertools.permutations(numbers)
        list = []
        for tp in res:
            result = ""
            for i in tp:
                result += str(i)
            list.append(result)
        list.sort()
        return list[0]

arr = [3,32,321]
import itertools
res = itertools.permutations(arr)
# print(list(res))
arr1 = [3]
print(Solution().PrintMinNumber(arr1))


