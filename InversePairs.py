# -*- coding:utf-8 -*-
import copy
class Solution:
    def InversePairs1(self, data):
        # write code here
        if len(data) == 1 or not data:
            return 0
        half = int(len(data)/2)
        left = self.InversePairs(data[:half])
        right = self.InversePairs(data[half:])
        across = self.findInverseAcrossArray(data)
        return (left + right + across) % 1000000007

    def findInverseAcrossArray(self,arr):
        half = int(len(arr)/2)
        cnt = 0
        for i in range(half):
            for j in range(half,len(arr)):
                if arr[i] > arr[j]:
                    cnt += 1
        return cnt


    def InversePairs(self,data):
        if not data or len(data) == 1:
            return 0
        sortedArr = copy.deepcopy(data)
        sortedArr.sort()
        result = 0
        for element in sortedArr:
            for i in range(len(data)):
                if data[i] == element:
                    result += i
                    data.pop(i)
                    break
        return result % 1000000007

if __name__ == "__main__":
    arr = [1,2,3,-2,5,6,7,0]
    arr1 = [3,4,2,8]
    print(Solution().InversePairs(arr))

# 思路

# 解法1
# 递归的解法，数组的逆序对数等于左子列，右子列，横跨左右的数组的逆序对数之和
# 考点：直接递归地写会超时，需要将递归改成循环（理论上所有递归和循环之间可以互换）

# 解法2
# 思路
# 将原问题分类，(1)将原数组按【从小到大】每次取一个元素，求该元素i作为逆序对中较小数求逆序数对x
# (2)将各个x相加得到最终结果
# 在计算机实现中，通过循环一步步将i前面小于i的数去掉了

# 两种思路都没问题，用java实现可以通过，但python实现总显示超时
