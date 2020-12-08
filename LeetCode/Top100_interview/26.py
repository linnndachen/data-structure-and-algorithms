class Solution:
    def use_pointer(self, nums: List[int]) -> int:
        pointer = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[pointer]:
                pointer += 1
                nums[pointer] = nums[i]
        return pointer+1

    def use_pop(self, nums):
        """
        I first tried to appraoch this problem by using pop. However,
        I got index out of range. I couldn't remebered my exact code now.
        I think it was because I put 'index += 1' within the if statement instead of
        just the else statement. Here's the correct answer.

        However, using pop is also not necessary in this case beacause the program
        automatically output the first x elements of indexes. Therefore, we only need to modify it. 
        """
        index = 1
        while index < len(nums):
            if nums[index] == nums[index-1]:
                nums.pop(index)
            else:
                index += 1
        return len(nums)

    def easy_to_read(self, nums):
        """
        In this solution, j servers as a pointer
        If numer at j index equals to the numer at i, then move the pointer.
        Else, meaning we found the next different numers, num[i+i] will become
        the unique number num[j]. We move to the next nums[i]
        """
        if len(nums) <= 1:
            return len(nums)
        i = 0
        j = i+1
        while j < len(nums):
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
        return i+1
