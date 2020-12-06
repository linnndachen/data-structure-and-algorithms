class Solution:
    def mysolution(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        else:
            for i in reversed(range(len(digits))):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    return digits
            return [1] + digits

    def solution_shorten(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


"""
Note:
At first, I negelected the problem of [9] or [9,9]
Then when I tried to sove it, I didn't remebered to use list+list. I was thinking so hard how to insert the 1. This is due to still being unfimilary with the data structure.

I think the key to this problem was to understand the possible circumstances. For example, I had redundant codes in my solution. 
"""
