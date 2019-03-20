# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number == 0 or number == 1:
            return number
        x,y = 1,2
        for i in range(3,number+1):
            t = y
            y += x
            x = t
        return y
if __name__ == "__main__":
    print(Solution().jumpFloor(7))
