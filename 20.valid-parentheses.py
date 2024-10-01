#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):

    def complement(self, s):
        if s == "(":
            return ")"
        elif s == "{":
            return "}"
        elif s == "[":
            return "]"


    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) == 0:
            return True
        elif len(s) == 0:
            return False

        for bracket in s:
            complement_bracket = self.complement(bracket)
            s = s[1:]
            found_comp = False
            for idx, next_bracket in enumerate(s):
                if next_bracket == complement_bracket:
                    found_comp = True
                    s = s[:idx] + s[idx:]
                    break
            if found_comp == False:
                return False




# @lc code=end

