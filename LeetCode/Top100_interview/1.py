class Solution:
    #40sec
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i, len(nums)):
                if nums[j] == diff:
                    return [i, j]

    def hash_table(self, nums, target):
        length = len(nums)
        table = {}
        for i in range(length):
            diff = target - nums[i]
            if diff in table:
                return [i, table[diff]]
            table[nums[i]] = i

