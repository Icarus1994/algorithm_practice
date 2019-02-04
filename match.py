import re

class Solution:

    def match(self, s, pattern):
        def fullmatch(regex, string, flags=0):
            return re.match("(?:" + regex + r")\Z", string, flags=flags)

        return True if fullmatch(pattern, s) else False