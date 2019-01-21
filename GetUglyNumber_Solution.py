# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        arr = [1]
        if index == 1:
            return 1
        elif index <=0:
            return 0
        while len(arr) < index:
            i = 0
            while arr[i]*2 <= arr[-1]:
                i += 1
            M2 = arr[i]*2
            i = 0
            while arr[i]*3 <= arr[-1]:
                i +=1
            M3 = arr[i]*3
            i = 0
            while arr[i]*5 <= arr[-1]:
                i +=1
            M5 = arr[i]*5
            arr.append(min(M2,M3,M5))
        return arr[-1]
print(Solution().GetUglyNumber_Solution(3))


# 解法1
# 最笨的办法是，一直循环，判断某数是否是丑数，一直得到第N个丑数为止
# 判断某数x是否是丑数的方法：（1）如果x能被2整除，继续除以2，直到不能整除为止
# （2）对3，5执行和（1）中同样的操作，除完后判断商是否为1
# 解法2
# 思路：一个丑数可以由前一个丑数乘以2，3或5得到。创建一个含有丑数的数组
# 故已知一个丑数M时，记M2为M前面的所有丑数乘以2后大于M的最小数，类似的有M3,M5，下一个丑数为min{M2,M3,M5}
# 优化：寻找M2,M3,M5时不需要从头到M一个个计算，因为存有一系列丑数的数组是升序排列的