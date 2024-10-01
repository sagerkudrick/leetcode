#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for idx, item in enumerate(nums):
            for idx_2, item_2 in enumerate(nums):
                if item + item_2 == target and idx is not idx_2:
                    return [idx, idx_2]

        
# @lc code=end

