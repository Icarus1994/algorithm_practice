# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if not s:
            return 0
        sign = 1
        num = 0
        if s[0] == "-":
            sign = -1
        elif s[0] == "+":
            None
        elif "0" <= s[0] <= "9":
            num = ord(s[0]) - ord("0")
        else:
            return 0

        if len(s) >1:
            for i in s[1:]:
                if "0" <= i <= "9":
                    num = num * 10 + ord(i) - ord("0")
                else:
                    return 0
        return num * sign


result = Solution().StrToInt("-12")
print(result)


