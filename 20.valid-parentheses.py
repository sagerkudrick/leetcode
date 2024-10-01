#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # if s is empty, there's no unclosed brackets
        if len(s) == 0:
            return True
        
        # if s == 1, there's an unopened/unclosed bracket
        if len(s) == 1:
            return False

        # empty stack + matching bracket dict
        stack = []
        matching_brackets = {
            "[" : "]",
            "(" : ")",
            "{" : "}"
        }

        # for every character in our list
        # we add the opened bracket to our stack
        # or, if it's a closing bracket, check if it
        # has an opening bracket 
        for char in s:

            # add the opening bracket to stack
            if char in matching_brackets:
                stack.append(char)

            # it's a closing bracket, 
            # check if we have a opening bracket for it
            else:
                # we encounter a closing bracket with no opening ones
                if stack == []:
                    return False
                
                item = stack.pop() # get an opening bracket
                
                # if ) != matching_brackets["("] -> ) (False)
                if char != matching_brackets[item]:
                    return False
                
        # if there's still opening brackets in stack, it wasn't closed
        # if the stacks empty, all opening/closing brackets are done
        if len(stack) > 0:
            return False
        else:
            return True
                    


# @lc code=end

