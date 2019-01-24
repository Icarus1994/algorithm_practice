# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array or len(array) < 2:
            return []
        result = set()
        for i in array:
            if i in result:
                result.remove(i)
            else:
                result.add(i)
        if not result:
            return []
        return [result.pop(),result.pop()]

arr = [1,4]
solu = Solution()
print(solu.FindNumsAppearOnce(arr))
