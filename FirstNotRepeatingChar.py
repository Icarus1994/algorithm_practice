# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        dict = {}
        index = 0
        for letter in s:
            if dict.__contains__(letter):
                dict[letter] = 10010
            else:
                dict[letter] = index
            index += 1
        location = 10010
        for key in dict:
            if dict.get(key) < location:
                location = dict.get(key)
        return location if location < 10010 else -1

