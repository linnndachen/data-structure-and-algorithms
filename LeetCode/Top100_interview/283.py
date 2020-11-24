#O(n)
class Solution:
    """
    Do not return anything, modify nums in-place instead.
    """
    def moveZeroes_long(self, nums: List[int]) -> None:
        """
        we assume the first zero is at index 0, if the first one is not zero,
        the list will not chnage after the first iteration. We move the 
        first zero index to the next position.
        """
        first0 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = 0
                nums[first0] = temp
                first0 += 1
        return nums

    def moveZeroes_short(self, nums):
        first0 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[first0],nums[i] = nums[i],nums[first0]
                first0 +=1
    
    def sort_method(self, nums):
        nums.sort(key=bool, reverse=True)
        #nums.sort(key=lambda x: 1 if x == 0 else 0)
