class Solution:
    def solution_math(self, nums):
        """
        Time - n, Space - 1
        Time is n because suming up all the numbers costs n time. 
        """
        n = len(nums)
        return n*(n+1)//2 - sum(nums)

    def solution_sorting(self, nums):
        """
        Time - N(log(n))
        """
        nums.sort()
        # if the missing one was the last index
        if nums[-1] != len(nums):
            return len(nums)
        elif nums[0] != 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i] != i:
                return i

    def missingNumber(self, nums: List[int]) -> int:
        """
        Time - n, Space - n
        Time is actually n+n, because using set() actually takes n times since
        we insert each value using O(1) time. Another n is in the for loop
        Space is for stornig all the values
        """
        all_nums = len(nums) + 1
        set_init = set(nums)
        for n in range(all_nums):
            if n not in set_init:
                return n
