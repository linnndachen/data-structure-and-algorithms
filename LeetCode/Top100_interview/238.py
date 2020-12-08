class Solution:
    def space_N(self, nums: List[int]) -> List[int]:
        """
        In this method, we're slicing the list.
        We take the product of the left, then the right, then we times them together.
        Time - O(N)
        Space - O(N)
        """
        length = len(nums)
        L, R, answer = [0]*length, [0]*length, [0]*length
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i-1] * L[i-1]

        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = nums[i+1] * R[i+1]

        for i in range(length):
            answer[i] = L[i] * R[i]

        return answer

    def space_one(self, nums):
        length = len(nums)
        answer = [0] * length
        
        answer[0] = 1
        for i in range(1, length):
            answer[i] = nums[i - 1] * answer[i - 1]

        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer

    def slowest(self, nums):
        """
        This is the brute force, the slowest method with O(n^2) time complexity
        """
        nums_copy = nums.copy()
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            nums_copy[i] = product

        return nums_copy









    def orginal_wrong_answer(self, nums):
        """
        my original approach was to times everything together and then divide the each number. However, this approach will post problems.
        For example:
        [1, 0, 2] -> [0, 2, 0]
        [0,4,0] -> [0, 0, 0]
        To solve the first situation, I imposed a condition that turn all 0 to the product other than itsel and everything else to 0.
        However, I would not be able to solve the 2nd problem with this condition because the 2 zeros will become 2 fours.

        That being said, I have to tackle this problem face to face - take the product of everything other than the number itself.

        BTW, this question also not allowed to use division
        """
        product = 1
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                product *= nums[i]
                count += 1
        if count == 0:
            return nums

        if 0 in nums:
            nums = [product if i == 0 else 0 for i in nums]
        else:
            nums = [int(product/i) for i in nums]
        
        return nums