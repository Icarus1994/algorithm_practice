# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers.sort()
        numOfZero = numbers.count(0)
        start = numOfZero
        if numOfZero ==4:
            return True
        for i in range(start,len(numbers)-1):
            d = numbers[i+1] - numbers[i]
            if d == 0:
                return False
            elif d != 1:
                if numOfZero >= d-1:
                    numOfZero -= d - 1
                else:
                    return False
        return True

numbers = [1,2,3,0,0]
result = Solution().IsContinuous(numbers)
print(result)