#
# @lc app=leetcode id=14 lang=python
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        first_word = strs[0]
        rest_words = strs[1:]
        longest_matching = ""

        for idx in range(len(first_word) + 1):
            for word in rest_words:
                if first_word[:idx] == word[:idx]:
                    continue
                else:
                    return longest_matching
            longest_matching = first_word[:idx]
        return longest_matching



        



# @lc code=end

