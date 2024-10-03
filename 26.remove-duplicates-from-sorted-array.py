#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # non-decreasing order...
        # 1, 2, 3, 4, 5...
        # 1, 1, 1, 2 - > 1, 2, _, _
        # None -> 1 -> 1 (remove) -> 1 (remove) -> 2 (+= 1)

        head = None
        # iterate over each item in the List.
        # if we don't have a head, set it to the first item.
        # otherwise, check if it's the same...if it is, it's a duplicate, remove it
        # then move on to the next, incremeneting our size. 
        # We use nums[:] to create a shallow copy, as nums.remove(item)
        # doesn't shift the index, so we skip over items.
        for item in nums[:]:
            if head == item:
                # remove the duplicate
                nums.remove(item)
            else:
                head = item

        return len(nums)

# @lc code=end

