# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if size == 0 or not num or len(num) < size:
            return []
        # 窗口的左指针
        maxVal = max(num[:size])
        maxPoint = num[:size].index(maxVal)
        res = [maxVal]
        left = 1
        # 窗口的右指针i
        for i in range(size,len(num)):
            if left > maxPoint:
                maxVal = max(num[left:i+1])
                maxPoint = num[left:i+1].index(maxVal)
            elif num[i] >= maxVal:
                maxVal = num[i]
                maxPoint = i
            res.append(maxVal)
            left += 1
        return res
num = [2,3,4,2,6,2,5,1]
size = 8
result = Solution().maxInWindows(num,size)
print(result)


# 思路1
# 如代码所示，最大时间复杂度O(size*n)

# 思路2
# 参考讨论区双向队列