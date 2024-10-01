#
# @lc app=leetcode id=9 lang=python
#
# [9] Palindrome Number
#

# @lc code=start
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        palendrome = False
        x = str(x)

        while True:
            if len(x) == 1 or len(x) == 0:
                palendrome = True
                break
            if x[:1] == x[-1:]:
                x = x[1:-1]
            else:
                break

        return palendrome


# @lc code=end

