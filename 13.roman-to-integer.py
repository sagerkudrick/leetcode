#
# @lc app=leetcode id=13 lang=python
#
# [13] Roman to Integer
#

# @lc code=start

class Solution(object):
    def romanInts(self, s):
        if s == "I":
            return 1
        elif s == "V":
            return 5
        elif s == "X":
            return 10
        elif s == "L":
            return 50
        elif s == "C":
            return 100
        elif s == "D":
            return 500
        elif s == "M":
            return 1000        
        

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        romanInt = 0

        idx = 0
        while idx < len(s):
            num_1 = self.romanInts(s[idx])
            if idx < len(s) - 1:
                num_2 = self.romanInts(s[idx + 1])   

                if num_1 < num_2:
                    romanInt += (num_2 - num_1)
                    idx += 2
                    continue

            romanInt += num_1
            idx += 1

        return romanInt

# @lc code=end

