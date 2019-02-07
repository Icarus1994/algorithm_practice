class Solution:
    def match1(self, s, pattern):
        if not s and not pattern:
            return True
        elif not s and pattern:
            if len(pattern) == 2 and pattern[-1] == "*":
                return True
            else:
                return False
        elif not pattern and s:
            return False
        else:
            if len(pattern) > 1 and pattern[1] == "*":
                if pattern[0] != s[0] and pattern[0] != ".":
                    return self.match1(s,pattern[2:])
                else:
                    i = 2
                    j = 0
                    cntP = 0
                    cntS = 0
                    while i<len(pattern) and pattern[i] == s[0]:
                        cntP += 1
                        i += 1
                    while j < len(s) and s[j] == s[0]:
                        cntS += 1
                        j += 1
                    if cntP > cntS:
                        return False
                    else:
                        return self.match1(s[j:],pattern[i:])
            else:
                if pattern[0] == s[0] or pattern[0] == ".":
                    return self.match1(s[1:], pattern[1:])
                else:
                    return False

    def match(self, s, pattern):
        if len(s) == 0 and len(pattern) == 0:
            return True
        elif len(pattern) == 0 and len(s) != 0:
            return False
        elif len(s) == 0 and len(pattern) != 0:
            if len(pattern) > 1 and pattern[1] == "*":
                return self.match(s,pattern[2:])
            else:
                return False
        else:
            if len(pattern) > 1 and pattern[1] == "*":
                if pattern[0] != s[0] and pattern[0] != ".":
                    return self.match(s, pattern[2:])
                else:
                    # 分为*前取0个、1个、多个字符的情况。
                    return self.match(s,pattern[2:]) or self.match(s[1:],pattern[2:]) or self.match(s[1:],pattern)
            else:
                if pattern[0] == s[0] or pattern[0] == ".":
                    return self.match(s[1:], pattern[1:])
                else:
                    return False


s = "a"
p = "aa.a"
p1 = "ab*ac*a"
p3 = ".*"
result = Solution().match("a", ".*")
print(result)
print("a"[1:],",",type("a"[1:]))
# note
# print(s[3:])

# 思路
# 分类判断法，*和.是引起问题不确定的因素，但是*导致的情况更复杂，因此以*为主进行分类解决问题。
# 题目说*前面的字符可以出现任意次，指的是前面的第一个字符

# 总：注意
# 一开始使用c语言的思维，通过下标i和多重if else语句实现，但是当同时考虑s（或pattern）遍历完成后
# 另一字符串还没遍历完的情况，以及循环中需要判断下一个字符是否为"*"的情况，if else会很复杂，
# 后来参考答案，使用Python切片+尾递归解决了该问题
# 如： s = "a*"时,s[2:]为None，不会报错

# 但match1没考虑到".*"的情况。eg.考虑用例"ab",".*",".*"等价于"..*",所以应该return True，


