#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # initialize lists
        return_list = None
        head_list = None     

        # while our two inputs aren't empty:
        while list1 != None and list2 != None:
            list_temp = None

            # get our lowest value, and move node to next
            if list1.val < list2.val:
                list_temp = list1
                list1 = list1.next

            elif list2.val < list1.val:
                list_temp = list2
                list2 = list2.next

            # they're equal, just use 2nd nodes value
            elif list2.val == list1.val:
                list_temp = list2
                list2 = list2.next

            # make sure our ListNode is initialized, otherwise add
            if return_list == None:
                return_list = ListNode(list_temp.val, None)
                head_list = return_list
            else:
                return_list.next = ListNode(list_temp.val, None)
                return_list = return_list.next

        # if a ListNode is empty and the other isn't, append it to ours
        # else statements handle a case where we get a None and non-Non at the
        # start, so we just return that ListNode
        if list1 != None:
            if return_list:
                return_list.next = list1
            else:
                return_list = list1
                head_list = return_list

        if list2 != None:
            if return_list:
                return_list.next = list2
            else:
                return_list = list2
                head_list = return_list


        return head_list

# @lc code=end