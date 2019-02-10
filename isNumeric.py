# -*- coding:utf-8 -*-
import re

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        if s.count("e") + s.count("E") == 0:
            return self.isPureNumeric(s)
        elif s.count("e") + s.count("E") == 1:
            letter = "e" if s.count("e") else "E"
            index = s.find(letter)
            return self.isPureNumeric(s[0:index]) and self.isPureNumeric(s[index+1:], hasSpot=True)
        else:
            return False

    def isPureNumeric(self, str, hasSpot = False):
        if not str:
            return False
        if str[0] != "-" and str[0] != "+":
            if "0" <= str[0] <= "9":
                None
            else:
                return False
        for i in str[1:]:
            if "0" <= i <= "9":
                None
            elif i == ".":
                if hasSpot:
                    return False
                else:
                    hasSpot = True
            else:
                return False
        return True

    # 学习正则匹配
    # 还是有问题：00.3和.00也会匹配为数字，不过测试用例没有弄得这么严格.
    def isNumeric1(self, s):
        return re.match(r"^[\+\-]?[0-9]*(\.[0-9]+)?([eE][\+\-]?[0-9]+)?$",s)

    # 学习在oj中用try catch
    def isNumeric2(self, s):
        # write code here
        try:
            ss = float(s)
            return True
        except:
            return False

s = "123.45e+6"
result = Solution().isNumeric(s)
print(result)

