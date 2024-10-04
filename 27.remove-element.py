#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # [1, 2, 3, 4, 5, 6]
        # 

        head = 0
        for x in range(len(nums)):
            if nums[x] != val:
                nums[head] = nums[x]
                head += 1


        return head 


# @lc code=end

